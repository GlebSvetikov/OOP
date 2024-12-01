import pymysql

class DBConnection:
    _instance = None

    def __new__(cls, host, user, password, database):
        """Метод для создания единственного экземпляра."""
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._init_connection(host, user, password, database)
        return cls._instance

    def _init_connection(self, host, user, password, database):
        """Инициализация соединения с базой данных."""
        self.connection = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            cursorclass=pymysql.cursors.DictCursor
        )

    def get_connection(self):
        """Метод для получения соединения с базой данных."""
        return self.connection

    def close(self):
        """Закрытие соединения."""
        if self.connection:
            self.connection.close()
            self._instance = None
