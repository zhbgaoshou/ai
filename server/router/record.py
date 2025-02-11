from datetime import datetime
from typing import Any
from fastapi import APIRouter, Body, Request, Depends, HTTPException
from sqlmodel.ext.asyncio.session import AsyncSession
from sqlmodel import select
from models.record import RecordIn, RecordOut, Record
import uuid
from dependencies import get_session, get_page


router = APIRouter()


# 生成标题
@router.post("/generate_title")
def get_record(request: Request, input_text: str = Body(..., embed=True)):
    client = request.app.state.openai_client
    prompt = f"Please generate a short title for the following text: {input_text}"
    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {
                "role": "user",
                "content": [{"type": "text", "text": prompt}],
            }
        ],
    )
    title = completion.choices[0].message.content.strip()
    return {"title": title}


# 创建记录
@router.post("", response_model=RecordOut)
async def create_record(record: Record, session: AsyncSession = Depends(get_session)):
    db_record = Record.model_validate(record)
    db_record.id = record.id
    if not db_record.id:
        db_record.id = uuid.uuid4().hex

    session.add(db_record)
    await session.commit()
    await session.refresh(db_record)

    return db_record


# 获取记录
@router.get("", response_model=dict[str, Any])
async def get_records(
    *,
    session: AsyncSession = Depends(get_session),
    user_id: int | str,
    name: str = "",
    page_data: dict = Depends(get_page),
):
    page_size = (page_data.get("offset") - 1) * page_data.get("limit")
    records = await session.exec(
        select(Record)
        .where(Record.user_id == user_id, Record.name.like(f"%{name}%"))
        .order_by(Record.created_at.desc(), Record.id.desc())
        .offset(page_size)
        .limit(page_data.get("limit") + 1)
    )
    list_records = records.all()

    # 判断是否有下一页
    has_next = len(list_records) > page_data.get("limit")
    if has_next:
        list_records = list_records[:-1]  # 移除多查询的一条数据

    return {
        "next": has_next,
        "data": list_records,
    }


# 删除会话
@router.delete("/{record_id}")
async def delete_record(
    record_id: int | str, session: AsyncSession = Depends(get_session)
):
    record = await session.get(Record, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="记录不存在")
    await session.delete(record)
    await session.commit()
    return {"id": record_id}


# 更新会话
@router.put("/{record_id}", response_model=RecordOut)
async def update_record(
    record_id: int | str,
    record: RecordIn,
    session: AsyncSession = Depends(get_session),
):
    db_record = await session.get(Record, record_id)
    if not db_record:
        raise HTTPException(status_code=404, detail="记录不存在")
    record_data = record.model_dump(exclude_unset=True)
    db_record.sqlmodel_update(record_data)
    db_record.updated_at = datetime.now()
    session.add(db_record)
    await session.commit()
    await session.refresh(db_record)
    return db_record


@router.get("/toggle")
async def toggle_record(
    session: AsyncSession = Depends(get_session), record_id: int | None | str = None
):
    """
    切换默认记录。

    - 如果提供了 record_id，则将其设置为默认记录，且取消当前默认记录。
    - 如果没有提供 record_id，则仅取消当前默认记录。
    """
    # 查询当前默认记录
    active_record = await session.exec(select(Record).where(Record.is_active == True))
    active_record = active_record.first()

    if record_id:  # 当提供了记录 ID 时
        # 查找待切换的记录
        record = await session.get(Record, record_id)
        if not record:
            raise HTTPException(status_code=404, detail="待切换的记录不存在")

        # 取消当前默认记录
        if active_record:
            active_record.is_active = False
            session.add(active_record)

        # 设置新的默认记录
        record.is_active = True
        session.add(record)
        await session.commit()
        return {"message": "切换默认记录成功"}

    else:  # 当未提供记录 ID 时
        if active_record:  # 存在默认记录
            active_record.is_active = False
            session.add(active_record)
            await session.commit()
            return {"message": "取消默认记录成功"}
        else:  # 不存在默认记录且未提供记录 ID
            raise HTTPException(
                status_code=400, detail="未提供记录 ID，且不存在默认记录"
            )
