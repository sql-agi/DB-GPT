from agents import ChatDBAgent
from web.app.models import ChatDBRequest, SessionTitle
from web.app.utils import DBUtil
from typing import Dict, Any, List

db_manager = DBUtil.get_db_manager()


class ChatDBService:

    @classmethod
    async def save_session(cls, session_title: SessionTitle) -> int:
        """
        保存会话，返回session_id
        """
        user_input = session_title.input
        database_id = session_title.database_id
        model = session_title.model
        session_id = db_manager.insert_chat_session(database_id, model, user_input)
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
        is_change = chat_db_request.is_change
        if is_change:
            database_id = chat_db_request.database_id
            model = chat_db_request.model
            db_manager.update_chat_session(session_id, database_id, model)
        else:
            session_info = db_manager.fetch_database_id_and_model(session_id)
            database_id = session_info['database_id']
            model = session_info['model']
        db_manager.insert_chat_history(session_id, database_id, model, "user", user_input)
        db_info = db_manager.get_database_by_id(database_id)
        db_url = DBUtil.create_mysql_url(db_info)
        reply = ChatDBAgent.chat_db(chat_db_request, db_url)
        if reply:
            db_manager.insert_chat_history(session_id, database_id, model, model, reply)
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
