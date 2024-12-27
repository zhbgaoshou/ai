from .base import BaseModel
from sqlmodel import SQLModel, Field


class Record(BaseModel, table=True):
    __tablename__ = "chat_record"
    name: str = Field(index=True)
    model: str
    user_id: int
    endpoint: str = Field(default=None)
    is_edited: bool = Field(default=False)
    is_active: bool = Field(default=False)


class RecordIn(SQLModel):
    name: str = Field(index=True)
    model: str
    user_id: int
    endpoint: str = Field(default=None)
    is_edited: bool = Field(default=False)
    is_active: bool = Field(default=False)


class RecordOut(BaseModel, RecordIn):
    pass
