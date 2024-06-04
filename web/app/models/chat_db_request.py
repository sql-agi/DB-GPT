from pydantic import BaseModel
from typing import Optional

class ChatDBRequest(BaseModel):
    database_id: int
    model: str
    input: str
    is_new_session: bool
    session_id: Optional[int] = None  # 使 session_id 成为可选参数，并默认为 None
