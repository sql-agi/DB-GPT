from fastapi import APIRouter, HTTPException
from web.app.models import ChatDBRequest, SessionTitle
from typing import List, Dict, Any
from web.app.service import ChatDBService

# 获取配置中的logger对象
from configs import log_config

logger = log_config.logger

router = APIRouter(
    prefix="/chat",
    tags=["error"],
    responses={404: {"description": "404 Not Found"}},
)

@router.post("/save-session")
async def save_session(session_title: SessionTitle) -> int:
    """
    保存会话，返回session_id
    """
    try:
        return await ChatDBService.save_session(session_title)
    except Exception as e:
        logger.error(f"Error in chat_db: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/db")
async def chat_db(chat_db_request: ChatDBRequest) -> str:
    """
     处理通过 POST 请求发送到 '/db' 路径的数据，并返回聊天生成的回复。
     此异步方法接收一个 JSON 格式的请求体，从中提取 'database_id'，'model' 和 'input' 字段，
     然后调用 `ChatDBService.chat_db` 方法处理这些输入，并返回处理结果。
     参数:
         chat_request (ChatRequestModel): 包含 'database_id'，'model' 和 'input' 字段的请求体。
     返回:
         dict: 包含键 'reply' 的字典，其值为处理输入得到的回复。
     抛出:
         HTTPException: 如果在处理请求或生成回复过程中发生任何异常，将返回500错误代码及异常详情。
     """
    try:
        return await ChatDBService.chat_db(chat_db_request)
    except Exception as e:
        logger.error(f"Error in chat_db: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/sessions", response_model=List[Dict[str, Any]])
async def fetch_all_chat_sessions() -> List[Dict[str, Any]]:
    """
    Retrieve all active chat sessions.
    """
    try:
        sessions = await ChatDBService.fetch_all_chat_sessions()
        return sessions
    except Exception as e:
        logger.error(f"Error fetching chat sessions: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.delete("/sessions/{session_id}", response_model=bool)
async def delete_chat_session(session_id: int) -> bool:
    """
    Delete a chat session and its related chat history.
    """
    try:
        result = await ChatDBService.delete_chat_session(session_id)
        return result
    except Exception as e:
        logger.error(f"Error deleting chat session: {e}")
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/history/{session_id}", response_model=List[Dict[str, Any]])
async def fetch_chat_history_by_session(session_id: int) -> List[Dict[str, Any]]:
    """
    Fetch chat history for a given session ID.
    """
    try:
        history = await ChatDBService.fetch_chat_history_by_session(session_id)
        return history
    except Exception as e:
        logger.error(f"Error fetching chat history: {e}")
        raise HTTPException(status_code=500, detail=str(e))
