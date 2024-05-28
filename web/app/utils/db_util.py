# utils/db_util.py
from web.app.dao import DBManager


class DBUtil:
    _db_manager = None

    @classmethod
    def get_db_manager(cls):
        if cls._db_manager is None:
            cls._db_manager = DBManager()
        return cls._db_manager
