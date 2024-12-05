import pymysql
from pymysql.cursors import DictCursor
import threading


class DBConnection:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, host, user, password, database, port=3306):
        with cls._lock:
            if cls._instance is None:
                cls._instance = super(DBConnection, cls).__new__(cls)
                cls._instance.connection = pymysql.connect(
                    host=host,
                    user=user,
                    password=password,
                    database=database,
                    port=port,
                    cursorclass=DictCursor
                )
                cls._instance._create_table_if_not_exists()
        return cls._instance

    def get_connection(self):
        return self.connection

    def close(self):
        with self._lock:
            if self._instance:
                self.connection.close()
                DBConnection._instance = None

    def _create_table_if_not_exists(self):
        create_table_query = """
        CREATE TABLE IF NOT EXISTS products (
            product_id INT NOT NULL AUTO_INCREMENT,
            name VARCHAR(255) NOT NULL,
            description TEXT,
            price DECIMAL(10,2) NOT NULL,
            stock_quantity INT NOT NULL,
            material VARCHAR(255) DEFAULT NULL,
            product_code VARCHAR(6) NOT NULL,
            UNIQUE (`product_code`),
            PRIMARY KEY (product_id),
            CHECK (CHAR_LENGTH(product_code) = 6)  
        )
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(create_table_query)
                self.connection.commit()
        except Exception as e:
            print(f"Ошибка при создании таблицы: {e}")
            self.connection.rollback()

