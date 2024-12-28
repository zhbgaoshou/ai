from .base import BaseModel
from sqlmodel import Field, SQLModel


class Model(BaseModel, table=True):
    __tablename__ = "chat_model"
    name: str
    value: str = Field(index=True)
    endpoint: str | None = Field(default=None)
    is_vip: bool = Field(default=False)
    description: str | None = Field(default=None)
    image: str | None = Field(default=None)
    default_model: bool = Field(default=False)


class ModelIn(SQLModel):
    name: str = Field(index=True)
    value: str
    endpoint: str | None = Field(default=None)
    is_vip: bool = Field(default=False)
    description: str | None = Field(default=None)
    image: str | None = Field(default=None)
    default_model: bool = Field(default=False)


class ModelOut(BaseModel, ModelIn):
    pass
