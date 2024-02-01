from pydantic import BaseModel

class Contact_user(BaseModel):
    name: str
    email: str
    phone:int
    city:str

class Del_data(BaseModel):
    id:int


class updateuser(BaseModel):
    id:int
    name:str
    email:str
    phone:int
    city:str