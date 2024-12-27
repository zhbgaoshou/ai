from fastapi import FastAPI
from router import record
from openai import OpenAI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

load_dotenv()


async def lifespan(app: FastAPI):
    # 在应用启动时初始化 OpenAI 客户端
    client = OpenAI(
        base_url=os.getenv("OPENAI_BASE_URL"),
        api_key=os.getenv("API_KEY"),
    )
    app.state.client = client
    yield
    print("应用程序关闭")


app = FastAPI(lifespan=lifespan)

app.include_router(record.router, prefix="/chat/record", tags=["record"])

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
