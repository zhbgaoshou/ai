from datetime import datetime
from sqlmodel import SQLModel, Field


class BaseModel(SQLModel):
    id: str | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = Field(default=None)

    # class Config:
    #     json_encoders = {
    #         datetime: lambda v: v.strftime("%Y-%m-%d %H:%M:%S"),
    #     }
