from pydantic import BaseModel


class UserPrompt(BaseModel):
    input: str
