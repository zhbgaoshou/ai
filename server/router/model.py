from datetime import datetime
from typing import Any
from fastapi import APIRouter, Body, Request, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from models.model import Model, ModelIn, ModelOut, ModelUserLink
from dependencies import get_session
import uuid


router = APIRouter()


@router.post("", response_model=ModelOut)
async def create_model(model: ModelIn, session: AsyncSession = Depends(get_session)):
    db_model = Model.model_validate(model)
    db_model.id = uuid.uuid4().hex
    session.add(db_model)
    await session.commit()
    await session.refresh(db_model)
    return db_model


@router.get("", response_model=list[ModelOut])
async def get_models(
    session: AsyncSession = Depends(get_session),
):
    models = await session.exec(select(Model))
    return models.all()


@router.put("/{model_id}", response_model=ModelOut)
async def update_model(
    model_id: int | str,
    model: ModelIn,
    session: AsyncSession = Depends(get_session),
):
    db_model = await session.get(Model, model_id)
    if not db_model:
        raise HTTPException(status_code=404, detail="模型不存在")
    model_data = model.model_dump(exclude_unset=True)
    db_model.sqlmodel_update(model_data)
    db_model.updated_at = datetime.now()
    await session.commit()
    await session.refresh(db_model)
    return db_model


@router.delete("/{model_id}")
async def delete_model(
    model_id: int | str,
    session: AsyncSession = Depends(get_session),
):
    db_model = await session.get(Model, model_id)
    if not db_model:
        raise HTTPException(status_code=404, detail="模型不存在")
    await session.delete(db_model)
    await session.commit()
    return {"message": "模型已删除"}


@router.post("/model_user_link", summary="模型和用户的关联表，用户是拥有这个模型的权限")
async def add_default_model(
    *,
    session: AsyncSession = Depends(get_session),
    model_name: str = Body(embed=True),
    user_id: int | str = Body(embed=True)
):
    db_data = ModelUserLink(model_name=model_name, user_id=user_id, id=uuid.uuid4().hex)
    session.add(db_data)
    await session.commit()
    await session.refresh(db_data)

    return db_data
