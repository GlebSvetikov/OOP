import psycopg2
from psycopg2.extensions import connection
from typing import Optional

class PostgreSQLConnection:
    _instance: Optional['PostgreSQLConnection'] = None
    _connection: Optional[connection] = None

    def __init__(self):
        """Private constructor."""
        if PostgreSQLConnection._instance is not None:
            raise Exception("This class is a singleton!")
        else:
            self._connection = None
            PostgreSQLConnection._instance = self

    @staticmethod
    def get_instance() -> 'PostgreSQLConnection':
        """Get singleton instance."""
        if PostgreSQLConnection._instance is None:
            PostgreSQLConnection._instance = PostgreSQLConnection()
        return PostgreSQLConnection._instance

    def get_connection(self) -> connection:
        """Get database connection."""
        if self._connection is None or self._connection.closed:
            self._connection = psycopg2.connect(
                database="products_db",
                user="postgres",
                password="postpass",
                host="localhost",
                port="5432"
            )
        return self._connection

    def close(self) -> None:
        """Close database connection."""
        if self._connection and not self._connection.closed:
            self._connection.close()
            self._connection = None