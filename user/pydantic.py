from pydantic import BaseModel

class Contact_user(BaseModel):
    name: str
    email: str
    phone:int
    city:str