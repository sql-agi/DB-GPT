
from fastapi import APIRouter, Request, HTTPException
from web.app.service import DBGptService

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
    async def db_gpt(request: Request):
        try:
            body = await request.json()
            reply = DBGptService.db_gpt(body.get('input'))
            return {"reply": reply}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))