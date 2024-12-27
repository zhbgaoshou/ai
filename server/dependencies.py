from database.mysql import engine
from sqlmodel import Session
from fastapi import Query


def get_session():
    with Session(engine) as session:
        yield session


def get_page(
    offset: int = Query(default=0, alias="page"),
    limit: int = Query(default=10, le=100, alias="page_size"),
):
    return {"offset": offset, "limit": limit}
