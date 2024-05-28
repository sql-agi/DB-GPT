from pydantic import BaseModel


class ChatDBRequest(BaseModel):
    database_id: int
    model: str
    input: str
