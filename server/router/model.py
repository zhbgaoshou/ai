from datetime import datetime
from typing import Any
from fastapi import APIRouter, Body, Request, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from models.model import Model, ModelIn, ModelOut
from dependencies import get_session


router = APIRouter()


@router.post("", response_model=ModelOut)
async def create_model(model: ModelIn, session: AsyncSession = Depends(get_session)):
    db_model = Model.model_validate(model)
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
    model_id: int,
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
    model_id: int,
    session: AsyncSession = Depends(get_session),
):
    db_model = await session.get(Model, model_id)
    if not db_model:
        raise HTTPException(status_code=404, detail="模型不存在")
    await session.delete(db_model)
    await session.commit()
    return {"message": "模型已删除"}


@router.get("/default", response_model=ModelOut)
async def get_default_model(session: AsyncSession = Depends(get_session)):
    model = await session.exec(select(Model).where(Model.default_model == True))
    return model.first()
