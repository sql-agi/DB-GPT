from fastapi import APIRouter, HTTPException
from web.app.service import DatabaseService
from web.app.models import DatabaseConnection
from typing import List, Dict, Any
import traceback

# 获取配置中的logger对象
from configs import log_config

logger = log_config.logger

router = APIRouter(
    prefix="/database",
    tags=["error"],
    responses={404: {"description": "404 Not Found"}},
)


@router.post("/save")
async def save_database(connection: DatabaseConnection) -> Any:
    """
    Handles POST requests sent to '/database/save' to save a database connection.
    This asynchronous method accepts a JSON formatted request body,
    which is validated against the DatabaseConnection Pydantic model.
    It then calls the `DatabaseService.save_database` method to save the data to the database.

    Parameters:
        connection (DatabaseConnection): Pydantic model that includes all the necessary fields.

    Returns:
        int: The ID of the newly saved database connection.

    Raises:
        HTTPException: If any exception occurs during the request processing or database operation,
        a 500 error code along with the exception details will be returned.
    """
    try:
        logger.info("database-save 请求参数: %s", connection.dict())
        return await DatabaseService.save_database(connection.dict())
    except Exception as e:
        logger.error("保存数据库连接时出错: %s", str(e))
        traceback_str = ''.join(traceback.format_tb(e.__traceback__))
        logger.error("Traceback: %s", traceback_str)
        raise HTTPException(status_code=500, detail=f"Exception: {e}, Traceback: {traceback_str}")


@router.delete("/delete/{connection_id}")
async def delete_database(connection_id: int) -> bool:
    """
    Handles DELETE requests sent to '/database/delete/{connection_id}' to delete a database connection by ID.

    Parameters:
        connection_id (int): The ID of the database connection to delete.

    Returns:
        bool: True if the deletion was successful, False otherwise.

    Raises:
        HTTPException: If any exception occurs during the request processing or database operation,
        a 500 error code along with the exception details will be returned.
    """
    try:
        return await DatabaseService.delete_database(connection_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.put("/update/{connection_id}")
async def update_database(connection_id: int, connection: DatabaseConnection) -> int:
    """
    Handles PUT requests sent to '/database/update/{connection_id}' to update an existing database connection by ID.

    Parameters:
        connection_id (int): The ID of the database connection to update.
        connection (DatabaseConnection): Pydantic model containing the updated fields.

    Returns:
        int: The ID of the updated database connection.

    Raises:
        HTTPException: If any exception occurs during the request processing or database operation,
        a 500 error code along with the exception details will be returned.
    """
    try:
        return await DatabaseService.update_database(connection_id, connection.dict())
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/list", response_model=List[Dict[str, Any]])
async def list_databases() -> List[Dict[str, Any]]:
    """
    Handles GET requests sent to '/database/list' to retrieve a list of all database connections.

    Returns:
        List[Dict[str, str]]: A list of dictionaries containing the id, database_name, and remark of all database connections.

    Raises:
        HTTPException: If any exception occurs during the request processing or database operation,
        a 500 error code along with the exception details will be returned.
    """
    try:
        return await DatabaseService.get_all_databases()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/{connection_id}", response_model=Dict[str, Any])
async def get_database_by_id(connection_id: int) -> Dict[str, Any]:
    """
    Handles GET requests sent to '/database/{connection_id}' to retrieve a database connection by its ID.

    Parameters:
        connection_id (int): The ID of the database connection to retrieve.

    Returns:
        Dict[str, Any]: The database connection details.

    Raises:
        HTTPException: If any exception occurs during the request processing or database operation,
        a 500 error code along with the exception details will be returned.
    """
    try:
        result = await DatabaseService.get_database_by_id(connection_id)
        if not result:
            raise HTTPException(status_code=404, detail="Database connection not found")
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

