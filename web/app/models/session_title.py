from pydantic import BaseModel


class SessionTitle(BaseModel):
    input: str
    database_id: int
    model: str
