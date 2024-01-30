from fastapi import APIRouter
from .pydantic import Contact_user
from .models import Contact

app = APIRouter()

@app.post('/reg_person/')
async def contact_detail(data:Contact_user):
    if await Contact.exists(email=data.email):
        return {'email already register'}

    elif await Contact.exists(mobilenum=data.phone):
        return {'phone already register'}
    
    else:
        obj = await Contact.create(name = data.name,email = data.email,
                             mobilenum = data.phone, city = data.city)
        return {'obj':obj}