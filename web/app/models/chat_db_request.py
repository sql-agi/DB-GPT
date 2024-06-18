from pydantic import BaseModel
from typing import Optional

class ChatDBRequest(BaseModel):
    database_id: Optional[int] = None
    model: Optional[str] = None
    input: str
    session_id: int
    is_change: bool

