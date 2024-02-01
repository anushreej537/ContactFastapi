from fastapi import APIRouter
from .pydantic import Contact_user,Del_data,updateuser
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
    

@app.get('/get_all_data')
async def all_detail():
    obj = await Contact.all()
    return (obj)


@app.delete('/deldata')
async def delete_data(data:Del_data):
    await Contact.get(id=data.id).delete()
    return {"messsage" : 'user delete successfully'}


@app.put("/updatedata")
async def update_user(data:updateuser):
    user_obj = await Contact.get(id=data.id)
    if not user_obj:
        return {"status":False, "message":"User Not found"}
    else:
        await Contact.filter(id=data.id).update(name=data.name,email=data.email,
                                              mobilenum=data.phone,city=data.city)
        return {"status":True, "message":"user update sucessfully"}