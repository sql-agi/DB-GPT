from pydantic import BaseModel


class AppBuilderRequest(BaseModel):
    input: str
    relate_info: str
