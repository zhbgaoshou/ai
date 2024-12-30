from database.mysql import engine
from sqlmodel.ext.asyncio.session import AsyncSession
from fastapi import Query


async def get_session():
    async with AsyncSession(engine) as session:
        yield session


def get_page(
    offset: int = Query(default=1, alias="page"),
    limit: int = Query(default=10, le=500, alias="page_size"),
):
    return {"offset": offset, "limit": limit}
