from fastapi import Request, HTTPException
from agents import ChatDBAgent


class DBGptService:

    @classmethod
    def  db_gpt(cls, input: str) -> str:
        """
        处理给定输入字符串，通过聊天数据库代理生成回复。

        此类方法接收一个字符串输入，通过 `ChatDBAgent.db_gpt` 方法来处理这个输入，并尝试返回生成的回复。
        如果在处理过程中遇到任何异常，会抛出 HTTP 异常。
        参数:
            input (str): 需要处理的输入字符串。
        返回:
            str: 聊天代理根据输入生成的回复。
        抛出:
            HTTPException: 如果在处理输入或生成回复的过程中发生异常，将返回状态码为500的HTTP异常，并包含异常的详细信息。
        """
        try:
            reply = ChatDBAgent.db_gpt(input)
            return reply
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
