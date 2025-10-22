from fastapi import FastAPI, APIRouter, Depends

router = APIRouter(prefix="/staff")

@router.get("/get-staff")
def get_staff():
    return {"msg": "Get Staff"}