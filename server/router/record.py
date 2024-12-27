from datetime import datetime
from fastapi import APIRouter, Body, Request, Depends, HTTPException
from sqlmodel import Session, select
from models.record import RecordIn, RecordOut, Record

from dependencies import get_session, get_page


router = APIRouter()


# 生成标题
@router.post("/generate_title")
def get_record(request: Request, input_text: str = Body(..., embed=True)):
    client = request.app.state.client

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


@router.post("", response_model=RecordOut)
def create_record(record: RecordIn, session: Session = Depends(get_session)):
    db_record = Record.model_validate(record)
    session.add(db_record)
    session.commit()
    session.refresh(db_record)

    return db_record


# 获取记录
@router.get("", response_model=list[RecordOut])
def get_records(
    *,
    session: Session = Depends(get_session),
    user_id: int,
    name: str = "",
    page_data: dict = Depends(get_page),
):
    records = session.exec(
        select(Record)
        .where(Record.user_id == user_id, Record.name.like(f"%{name}%"))
        .offset(page_data.get("offset"))
        .limit(page_data.get("limit"))
    ).all()
    return records


# 删除会话
@router.delete("/{record_id}")
def delete_record(record_id: int, session: Session = Depends(get_session)):
    record = session.get(Record, record_id)
    if not record:
        raise HTTPException(status_code=404, detail="记录不存在")
    session.delete(record)
    session.commit()
    return {"id": record_id}


# 更新会话
@router.put("/{record_id}", response_model=RecordOut)
def update_record(
    record_id: int,
    record: RecordIn,
    session: Session = Depends(get_session),
):
    db_record = session.get(Record, record_id)
    if not db_record:
        raise HTTPException(status_code=404, detail="记录不存在")
    record_data = record.model_dump(exclude_unset=True)
    db_record.sqlmodel_update(record_data)
    db_record.updated_at = datetime.now()
    session.add(db_record)
    session.commit()
    session.refresh(db_record)
    return db_record


@router.get("/toggle")
def toggle_record(
    session: Session = Depends(get_session), record_id: int | None = None
):
    """
    切换默认记录。

    - 如果提供了 record_id，则将其设置为默认记录，且取消当前默认记录。
    - 如果没有提供 record_id，则仅取消当前默认记录。
    """
    # 查询当前默认记录
    active_record = session.exec(select(Record).where(Record.is_active == True)).first()

    if record_id:  # 当提供了记录 ID 时
        # 查找待切换的记录
        record = session.get(Record, record_id)
        if not record:
            raise HTTPException(status_code=404, detail="待切换的记录不存在")

        # 取消当前默认记录
        if active_record:
            active_record.is_active = False
            session.add(active_record)

        # 设置新的默认记录
        record.is_active = True
        session.add(record)
        session.commit()
        return {"message": "切换默认记录成功"}

    else:  # 当未提供记录 ID 时
        if active_record:  # 存在默认记录
            active_record.is_active = False
            session.add(active_record)
            session.commit()
            return {"message": "取消默认记录成功"}
        else:  # 不存在默认记录且未提供记录 ID
            raise HTTPException(
                status_code=400, detail="未提供记录 ID，且不存在默认记录"
            )
