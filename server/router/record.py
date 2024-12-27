from fastapi import APIRouter, Body, Request, Depends
from sqlmodel import Session, select
from models.record import RecordIn, RecordOut, Record

from dependencies import get_session


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
