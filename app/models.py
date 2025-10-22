from .database import getDB 
from bson import ObjectId

def create_student_helper(data):
    return data

async def create_student(data:dict):
    document = create_student_helper(data)
    db = getDB()
    collection = db["students"]
    result = collection.insert_one(document)
    return {
        "inserted_id": str(result.inserted_id),
        "acknowledged": result.acknowledged
    }
