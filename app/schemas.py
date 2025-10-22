from pydantic import BaseModel

class StudentCreate(BaseModel):
    name:str
    phone:int
    dob:str
    hobbies:str
    country:str
    photo:str
