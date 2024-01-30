# from fastapi import FastAPI

# app=FastAPI()

# @app.get('/')
# async def contact():
#     return {'msg':'hello world'}


from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from user import api as UserAPI

app = FastAPI()

app.include_router(UserAPI.app)


register_tortoise(
    app,
    db_url="postgres://postgres:root@127.0.0.1/Contact",
    modules={'models': ['user.models',]},
    generate_schemas=True,
    add_exception_handlers=True
)