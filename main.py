
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from web.app.routes import database_route

app = FastAPI()

# 将origins设置为前端服务器的地址和端口
origins = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(database_route.router)

if __name__ == '__main__':
    uvicorn.run("main:app", host='0.0.0.0', port=8000, log_level="info")
    print("running")