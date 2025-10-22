from fastapi import FastAPI, APIRouter, Depends

router = APIRouter(prefix="/marks")

@router.get("/get-marks")
def get_marks():
    return {"msg": "Get Marks"}