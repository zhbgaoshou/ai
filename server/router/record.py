from fastapi import APIRouter, Body, Request


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
