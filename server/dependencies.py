from database.mysql import engine
from sqlmodel import Session
from fastapi import Query


def get_session():
    with Session(engine) as session:
        yield session
