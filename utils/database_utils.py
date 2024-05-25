# utils/database_utils.py
import os

class DatabaseUtils:
    """
    Utility class for database-related operations.
    """

    @staticmethod
    def create_mysql_url() -> str:
        """
        Assemble MySQL connection URL from environment variables.

        :return: MySQL connection URL as a string
        """
        host = os.getenv("MYSQL_HOST")
        port = os.getenv("MYSQL_PORT")
        user = os.getenv("MYSQL_USER")
        password = os.getenv("MYSQL_PASSWORD")
        database = os.getenv("MYSQL_DATABASE")
        return f"mysql://{user}:{password}@{host}/{database}"
