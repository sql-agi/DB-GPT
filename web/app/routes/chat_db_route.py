from fastapi import APIRouter, HTTPException
from web.app.models import ChatDBRequest
from typing import Dict
from web.app.service import ChatDBService

# 获取配置中的logger对象
from configs import log_config

logger = log_config.logger

router = APIRouter(
    prefix="/chat",
    tags=["error"],
    responses={404: {"description": "404 Not Found"}},
)


@router.post("/db")
async def chat_db(chat_db_request: ChatDBRequest) -> Dict[str, str]:
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
