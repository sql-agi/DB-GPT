from agents import ChatDBAgent
from web.app.models import ChatDBRequest, UserPrompt
from web.app.utils import DBUtil
from typing import Dict, Any, List

db_manager = DBUtil.get_db_manager()


class ChatDBService:

    @classmethod
    async def save_session(user_prompt: UserPrompt) -> int:
        """
        保存会话，返回session_id
        """
        user_input = user_prompt.input
        session_id = db_manager.insert_chat_session(user_input)
        return session_id

    @classmethod
    async def chat_db(cls, chat_db_request: ChatDBRequest) -> str:
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

        user_input = chat_db_request.input
        session_id = chat_db_request.session_id
        chat_history = db_manager.get_chat_history_by_session_id(session_id)
        if not chat_history:
            return "该聊天已被删除，请重新创建聊天！"
        db_manager.insert_chat_history(session_id, "user", user_input)

        database_id = chat_db_request.database_id
        db_info = db_manager.get_database_by_id(database_id)
        db_url = DBUtil.create_mysql_url(db_info)
        model = chat_db_request.model
        reply = ChatDBAgent.chat_db(db_url, model, user_input)
        if reply:
            db_manager.insert_chat_history(session_id, model, reply)
            return reply

    @classmethod
    async def fetch_all_chat_sessions(cls) -> List[Dict[str, Any]]:
        """
        Fetch all active chat sessions.
        :return: A list of dictionaries, each representing an active chat session.
        """
        chat_sessions = db_manager.get_chat_sessions_by_user_id()
        return chat_sessions

    @classmethod
    async def delete_chat_session(cls, session_id: int) -> bool:
        """
        Deletes a chat session and its related chat history records.
        :param session_id: The ID of the session to be deleted.
        :return: True if the chat session and all related chat history records are successfully deleted, otherwise False.
        """
        session_deleted = db_manager.delete_chat_session_by_id(session_id)
        if session_deleted:
            # If the session is successfully deleted, delete related chat history
            history_deleted = db_manager.delete_chat_history_by_session_id(session_id)
            return history_deleted
        return False

    @classmethod
    async def fetch_chat_history_by_session(cls, session_id: int) -> List[Dict[str, Any]]:
        """
        Fetch and return chat history for a given session ID.

        :param session_id: The ID of the session for which to retrieve chat history.
        :return: A list of dictionaries, each dictionary contains details about a chat message.
                 Returns an empty list if no chat history is found or if the session is deleted.
        """
        chat_history = db_manager.get_chat_history_by_session_id(session_id)
        return chat_history
