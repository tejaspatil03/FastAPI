from fastapi import FastAPI, APIRouter, Depends
from ..schemas import StudentCreate
from ..models import create_student


router = APIRouter(prefix="/students")

@router.get("/get-students")
def get_students():
    return "List of students"

@router.get("/get-profile")
def get_profile(uid:str):
    return f"Profile of {uid}"

@router.post("/save-std")
async def save_student(data:StudentCreate):
    stdDictObj = data.model_dump()
    print("..start")
    result = await create_student(stdDictObj)
    print("...",result)
    return result

@router.post("/login")
def login(user : str):
    return ""