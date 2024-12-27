from fastapi import FastAPI
from router import record

app = FastAPI()

app.include_router(record.router, prefix="/chat/record", tags=["record"])
