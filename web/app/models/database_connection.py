from pydantic import BaseModel
from typing import Optional


class DatabaseConnection(BaseModel):
    database_type: str
    database_name: str
    username: str
    password: str
    address: str
    port: int
    remark: Optional[str] = None
