from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_users():
    return {"message": "Users API is working!"}
