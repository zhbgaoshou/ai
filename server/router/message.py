from typing import AsyncGenerator, List, Dict
from fastapi import APIRouter, Request, Depends, Response
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from models.message import Message, MessageIn
from dependencies import get_session
import uuid
import json
from sse_starlette import EventSourceResponse
from fastapi.encoders import jsonable_encoder
from openai.types.chat import ChatCompletion
from openai import AsyncOpenAI

router = APIRouter()


class ChatService:
    """聊天服务类，处理聊天相关的业务逻辑"""

    def __init__(self, session: AsyncSession, client: AsyncOpenAI):
        self.session = session
        self.client = client

    async def get_chat_history(self, record_id: str, limit: int = 5) -> List[Message]:
        """获取聊天历史记录

        Args:
            record_id: 记录ID
            limit: 获取条数，默认5条

        Returns:
            List[Message]: 历史消息列表
        """
        query = (
            select(Message)
            .where(Message.record_id == record_id)
            .order_by(Message.created_at.desc())
            .offset(0)
            .limit(limit)
        )
        result = await self.session.exec(query)
        messages = result.all()
        messages.reverse()
        return messages

    def format_messages(
        self, history: List[Message], new_message: MessageIn
    ) -> List[Dict]:
        """格式化消息列表为OpenAI API所需格式

        Args:
            history: 历史消息列表
            new_message: 新消息

        Returns:
            List[Dict]: 格式化后的消息列表
        """
        system_prompt = {"role": "system", "content": "You are a helpful assistant."}
        history_messages = [
            {"role": msg.role, "content": msg.content} for msg in history
        ]
        user_message = {"role": "user", "content": new_message.content}

        return [system_prompt] + history_messages + [user_message]

    async def save_messages(
        self, user_message: str, ai_message: str, message_params: MessageIn
    ) -> tuple[Message, Message]:
        """保存用户消息和AI回复

        Args:
            user_message: 用户消息内容
            ai_message: AI回复内容
            message_params: 消息参数

        Returns:
            tuple[Message, Message]: 保存的用户消息和AI消息
        """
        user_id = uuid.uuid4().hex
        ai_id = uuid.uuid4().hex

        # 创建用户消息记录
        user_data = Message(
            id=user_id,
            content=user_message,
            ai_message_id=ai_id,
            role="user",
            unfinished=True,
            user_id=message_params.user_id,
            model=message_params.model,
            record_id=message_params.record_id,
        )

        # 创建AI消息记录
        ai_data = Message(
            id=ai_id,
            content=ai_message,
            user_message_id=user_id,
            role="assistant",
            unfinished=True,
            user_id=message_params.user_id,
            model=message_params.model,
            record_id=message_params.record_id,
        )

        # 保存消息
        self.session.add(user_data)
        await self.session.commit()
        self.session.add(ai_data)
        await self.session.commit()

        return user_data, ai_data


class StreamResponse:
    """流式响应处理类"""

    @staticmethod
    def set_headers(response: Response) -> None:
        """设置SSE响应头

        Args:
            response: FastAPI Response对象
        """
        response.headers["Content-Type"] = "text/event-stream"
        response.headers["Cache-Control"] = "no-cache"
        response.headers["Connection"] = "keep-alive"

    @staticmethod
    def create_response(text: str, finish: bool = False, data: dict = None) -> str:
        """创建SSE响应数据

        Args:
            text: 响应文本
            finish: 是否结束
            data: 额外数据

        Returns:
            str: JSON格式的响应数据
        """
        response = {
            "text": text,
            "finish": finish,
        }
        if data:
            response["data"] = data
        return json.dumps(response, ensure_ascii=False)


@router.post("/stream")
async def chat(
    request: Request,
    message: MessageIn,
    response: Response,
    session: AsyncSession = Depends(get_session),
) -> EventSourceResponse:
    """流式聊天接口

    Args:
        request: FastAPI请求对象
        message: 用户消息
        response: FastAPI响应对象
        session: 数据库会话

    Returns:
        EventSourceResponse: 流式响应
    """
    # 初始化服务
    chat_service = ChatService(session, request.app.state.openai_client)

    # 设置响应头
    StreamResponse.set_headers(response)

    # 获取历史记录
    history = await chat_service.get_chat_history(message.record_id)

    # 格式化消息
    send_messages = chat_service.format_messages(history, message)

    async def event_stream() -> AsyncGenerator[str, None]:
        ai_content = ""
        try:
            # 调用OpenAI API
            completion = chat_service.client.chat.completions.create(
                model=message.model,
                messages=send_messages,
                stream=True,
            )

            for chunk in completion:
                if chunk.choices:
                    delta_content = chunk.choices[0].delta.content
                    if delta_content:
                        ai_content += delta_content
                        yield StreamResponse.create_response(delta_content)
                else:
                    # 流式响应结束，保存消息
                    yield StreamResponse.create_response(
                        "", finish=True, data=chunk.dict()
                    )
                    await chat_service.save_messages(
                        message.content, ai_content, message
                    )

        except Exception as e:
            yield StreamResponse.create_response(
                "", finish=True, data={"error": str(e)}
            )

    return EventSourceResponse(event_stream())
