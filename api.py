
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from web.app.routes import db_gpt_route

app = FastAPI()

origins = ["http://localhost:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(db_gpt_route.router)

if __name__ == '__main__':
    uvicorn.run("api:app", host='127.0.0.1', port=8000, log_level="info")
    print("running")