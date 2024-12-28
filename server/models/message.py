from .base import BaseModel
from sqlmodel import Field, Relationship, SQLModel


class Message(BaseModel, table=True):
    __tablename__ = "chat_message"
    content: str
    unfinished: bool = Field(default=False)
    user_id: int | None = Field(default=None)
    is_copy: bool = Field(default=False)
    is_edited: bool = Field(default=False)
    role: str = Field(default="user")
    ai_message_id: str | None = Field(default=None)
    record_id: str = Field(index=True, foreign_key="chat_record.id")
    record: "Record" = Relationship(back_populates="messages")


class MessageIn(SQLModel):
    content: str
    user_id: int | None = Field(default=None)
    model: str = Field(default="gpt-3.5-turbo")
    role: str = Field(default="user")
    record_id: str = Field(index=True, foreign_key="chat_record.id")


class MessageOut(BaseModel):
    content: str
    unfinished: bool = Field(default=False)
    user_id: int | None = Field(default=None)
    is_copy: bool = Field(default=False)
    is_edited: bool = Field(default=False)
    role: str = Field(default="user")
    record_id: str = Field(index=True, foreign_key="chat_record.id")
