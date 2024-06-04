import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from web.app.routes import database_route, chat_db_route
from fastapi.openapi.utils import get_openapi


def db_gpt_api():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="DB-GPT API",
        version="v0.0.2",
        description="This is db-gpt api docs",
        routes=app.routes,
    )
    app.openapi_schema = openapi_schema
    return app.openapi_schema


app = FastAPI()
app.openapi = db_gpt_api

# 将origins设置为前端服务器的地址和端口
origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(database_route.router)
app.include_router(chat_db_route.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level="info")
    print("running")
