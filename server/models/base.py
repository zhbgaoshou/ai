from datetime import datetime
import time
from sqlmodel import SQLModel, Field
from sqlalchemy.types import DECIMAL
from sqlalchemy import Column


class BaseModel(SQLModel):
    id: str | None = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: datetime | None = Field(default=None)
    created_at_timestamp: float = Field(
        default_factory=time.time,
        sa_type=DECIMAL(20, 6),
    )
