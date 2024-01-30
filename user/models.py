from tortoise.models import Model
from tortoise import fields


class Contact(Model):
    name = fields.CharField(200)
    email = fields.CharField(250)
    mobilenum = fields.IntField()
    city = fields.CharField(200)

    

