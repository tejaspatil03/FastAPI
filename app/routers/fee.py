from fastapi import FastAPI, APIRouter, Depends

router = APIRouter(prefix="/fee")

@router.get("/get-fee")
def get_fee(name):
    return {"fee": "Fee details"}