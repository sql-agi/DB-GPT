from typing import Dict, Any, List
from web.app.utils import DBUtil

class DatabaseService:



    @classmethod
    async def save_database(cls, data: Dict[str, Any]) -> Any:
        """
        Saves a database connection using the given data.

        Parameters:
            data (Dict[str, Any]): The data for the database connection to be saved.

        Returns:
            int: The ID of the newly saved database connection.
        """
        db_manager = DBUtil.get_db_manager()
        existing_database = db_manager.get_database_by_name(data['database_name'])
        if existing_database:
            return "Database name already exists"
        connection_id = db_manager.save_database(data)
        return connection_id

    @classmethod
    async def delete_database(cls, connection_id: int) -> bool:
        """
        Deletes a database connection by its ID.

        Parameters:
            connection_id (int): The ID of the database connection to delete.

        Returns:
            bool: True if the deletion was successful, False otherwise.
        """
        db_manager = DBUtil.get_db_manager()
        success = db_manager.delete_database(connection_id)
        return success

    @classmethod
    async def update_database(cls, connection_id: int, data: Dict[str, Any]) -> int:
        """
        Updates a database connection with the given data.

        Parameters:
            connection_id (int): The ID of the database connection to update.
            data (Dict[str, Any]): The updated data for the database connection.

        Returns:
            int: The ID of the updated database connection.
        """
        db_manager = DBUtil.get_db_manager()
        updated_id = db_manager.update_database(connection_id, data)
        return updated_id

    @classmethod
    async def get_all_databases(cls) -> List[Dict[str, Any]]:
        """
        Retrieves a list of all database connections.

        Returns:
            List[Dict[str, str]]: A list of dictionaries containing the id, database_name, and remark of all database connections.
        """
        db_manager = DBUtil.get_db_manager()
        return db_manager.get_all_databases()

    @classmethod
    async def get_database_by_id(cls, connection_id: int) -> Dict[str, Any]:
        """
        Retrieves a database connection by its ID.

        Parameters:
            connection_id (int): The ID of the database connection to retrieve.

        Returns:
            Dict[str, Any]: A dictionary containing the details of the database connection.
        """
        db_manager = DBUtil.get_db_manager()
        return db_manager.get_database_by_id(connection_id)
