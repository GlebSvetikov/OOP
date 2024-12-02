import pymysql
from pymysql.cursors import DictCursor

class DBConnection:
    _instance = None

    def __new__(cls, host, user, password, database, port=3306):
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
        return cls._instance

    def get_connection(self):
        return self.connection

    def close(self):
        if self._instance:
            self.connection.close()
            DBConnection._instance = None

