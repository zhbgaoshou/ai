from fastapi import APIRouter

router = APIRouter()


@router.get("")
def get_record():
    return {"message": "get record"}
