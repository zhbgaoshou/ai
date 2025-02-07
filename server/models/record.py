from .base import BaseModel
from sqlmodel import Relationship, SQLModel, Field
from .message import Message


class Record(BaseModel, table=True):
    __tablename__ = "chat_record"
    name: str
    model: str
    user_id: int = Field(index=True)
    endpoint: str = Field(default=None)
    is_edited: bool = Field(default=False)
    is_active: bool = Field(default=False)
    messages: list["Message"] = Relationship(
        back_populates="record", cascade_delete=True
    )


class RecordIn(SQLModel):
    name: str
    model: str
    user_id: int
    endpoint: str = Field(default=None)
    is_edited: bool = Field(default=False)
    is_active: bool = Field(default=False)


class RecordOut(BaseModel, RecordIn):
    pass
