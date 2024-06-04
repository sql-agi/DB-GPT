# utils/db_util.py
from web.app.dao import DBManager


class DBUtil:
    _db_manager = None

    @classmethod
    def get_db_manager(cls):
        if cls._db_manager is None:
            cls._db_manager = DBManager()
        return cls._db_manager

    @classmethod
    def create_mysql_url(cls, db_info):
        """
        Assemble MySQL connection URL from provided database information.

        :param db_info: A dictionary containing the database connection details
        :return: MySQL connection URL as a string
        """
        user = db_info.get('username')
        password = db_info.get('password')  # Assuming password is included in db_info
        host = db_info.get('address')
        port = db_info.get('port')
        database = db_info.get('database_name')
        return f"mysql://{user}:{password}@{host}:{port}/{database}"