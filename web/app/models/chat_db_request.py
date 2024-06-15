from pydantic import BaseModel
from typing import Optional

class ChatDBRequest(BaseModel):
    database_id: int
    model: str
    input: str
    session_id: int
