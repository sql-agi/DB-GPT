from fastapi import Request, HTTPException
from agents import ChatDBAgent


class DBGptService:

    @classmethod
    def db_gpt(cls, input: str):
        try:
            reply = ChatDBAgent.db_gpt(input)
            return reply
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
