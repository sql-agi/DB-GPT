from fastapi import APIRouter, Request, HTTPException
from web.app.service import DBGptService
from typing import Dict
from web.app.models import AppBuilderRequest
import traceback

# 获取配置中的logger对象
from configs import log_config
logger = log_config.logger

router = APIRouter(
    prefix="/chat",
    tags=["error"],
    responses={404: {"description": "404 Not Found"}},
)


class DBGptRoute:
    @router.post("/db")
    async def db_gpt(request: Request) -> Dict[str, str]:
        """
         处理通过 POST 请求发送到 '/db' 路径的数据，并返回聊天生成的回复。
         此异步方法接收一个 JSON 格式的请求体，从中提取 'input' 字段作为输入，
         然后调用 `DBGptService.db_gpt` 方法处理这个输入，并返回处理结果。
         参数:
             request (Request): FastAPI的请求对象，包含客户端发送的HTTP请求信息。
         返回:
             dict: 包含键 'reply' 的字典，其值为处理输入得到的回复。
         抛出:
             HTTPException: 如果在处理请求或生成回复过程中发生任何异常，将返回500错误代码及异常详情。
         """
        try:
            body = await request.json()
            reply = await DBGptService.db_gpt(body.get('input'))
            return {"reply": reply}
        except Exception as e:
            logger.error("chat/db出错: %s", str(e))
            traceback_str = ''.join(traceback.format_tb(e.__traceback__))
            logger.error("Traceback: %s", traceback_str)
            raise HTTPException(status_code=500, detail=f"Exception: {e}, Traceback: {traceback_str}")


    @router.post("/db-appbuilder")
    async def chat_db_by_app_builder(app_builder_request: AppBuilderRequest) -> str:
        """
         处理通过 POST 请求发送到 '/db' 路径的数据，并返回聊天生成的回复。
         此异步方法接收一个 JSON 格式的请求体，从中提取 'input' 字段作为输入，
         然后调用 `DBGptService.db_gpt` 方法处理这个输入，并返回处理结果。
         参数:
             request (Request): FastAPI的请求对象，包含客户端发送的HTTP请求信息。
         返回:
             dict: 包含键 'reply' 的字典，其值为处理输入得到的回复。
         抛出:
             HTTPException: 如果在处理请求或生成回复过程中发生任何异常，将返回500错误代码及异常详情。
         """
        try:
            return await DBGptService.chat_db_by_app_builder(app_builder_request)
        except Exception as e:
            logger.error("chat/db-appbuilder出错: %s", str(e))
            traceback_str = ''.join(traceback.format_tb(e.__traceback__))
            logger.error("Traceback: %s", traceback_str)
            raise HTTPException(status_code=500, detail=f"Exception: {e}, Traceback: {traceback_str}")
