from .base import BaseModel
from sqlmodel import Field, Relationship, SQLModel
from sqlalchemy import Column, Text


class Message(BaseModel, table=True):
    __tablename__ = "chat_message"
    content: str = Field(sa_column=Column(Text))
    unfinished: bool = Field(default=False)
    user_id: int | None = Field(default=None)
    is_copy: bool = Field(default=False)
    is_edited: bool = Field(default=False)
    role: str = Field(default="user")
    ai_message_id: str | None = Field(default=None)
    user_message_id: str | None = Field(default=None)
    record_id: str = Field(index=True, foreign_key="chat_record.id")
    model: str = Field(default="gpt-3.5-turbo")
    record: "Record" = Relationship(back_populates="messages")


class MessageIn(SQLModel):
    content: str = Field(sa_column=Column(Text))
    user_id: int | None = Field(default=None)
    model: str = Field(default="gpt-3.5-turbo")
    role: str = Field(default="user")
    record_id: str = Field(index=True, foreign_key="chat_record.id")
    endpoint: str = Field(default=None)


class MessageOut(BaseModel):
    content: str = Field(sa_column=Column(Text))
    unfinished: bool = Field(default=False)
    user_id: int | None = Field(default=None)
    is_copy: bool = Field(default=False)
    is_edited: bool = Field(default=False)
    role: str = Field(default="user")
    record_id: str = Field(index=True, foreign_key="chat_record.id")
    ai_message_id: str | None = Field(default=None)
    user_message_id: str | None = Field(default=None)
    model: str = Field(default="gpt-3.5-turbo")
