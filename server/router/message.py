from datetime import datetime
from typing import Any, AsyncGenerator
from fastapi import (
    APIRouter,
    Body,
    Request,
    Depends,
    HTTPException,
    responses,
    Response,
)
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from models.message import Message, MessageIn, MessageOut
from dependencies import get_session
import uuid
import json


router = APIRouter()


# 按流式响应处理
@router.post("/stream")
async def chat(
    request: Request,
    message: MessageIn,
    response: Response,
    session: AsyncSession = Depends(get_session),
):
    """
    一个流式响应的 OpenAI Chat Completion 接口。
    """
    # 设置响应头
    response.headers["Content-Type"] = "text/event-stream"
    response.headers["Cache-Control"] = "no-cache"
    response.headers["Connection"] = "keep-alive"

    # 获取 OpenAI 客户端（假设已在 app.state 中初始化）
    client = request.app.state.openai_client

    # 调用 OpenAI 的聊天接口，启用流式数据传输
    completion = client.chat.completions.create(
        model=message.model,
        messages=[
            {"role": "developer", "content": "You are a helpful assistant."},
            {"role": "user", "content": "你好啊!"},
        ],
        stream=True,  # 开启流式模式
    )

    # 定义生成器函数，用于流式发送数据
    async def event_stream() -> AsyncGenerator[str, None]:
        try:
            for chunk in completion:  # 遍历流式响应的内容
                # 从 `chunk` 获取数据
                choices = chunk.choices  # 获取选项
                if choices:
                    text = choices[0].delta.content  # 获取文本内容
                    if text and text != "None":  # 如果文本存在且不为 "None"
                        res_json = {"text": text, "finish": False}
                        yield json.dumps(res_json)
                else:  # 如果没有选择内容，标记完成
                    res_json = {"finish": True, "data": chunk.dict()}
                    yield json.dumps(res_json)
        except Exception as e:  # 异常处理
            error_message = {"error": str(e), "finish": True}
            yield json.dumps(error_message)  # 返回错误信息

    # 返回一个流式响应
    return responses.StreamingResponse(event_stream(), media_type="text/event-stream")
