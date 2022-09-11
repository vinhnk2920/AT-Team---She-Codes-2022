import dotenv
from peewee import *

db = MySQLDatabase('at_manage', host="localhost", port=3306, user='root', passwd='vinh629220')
db.connect()


class BaseModel(Model):
    class Meta:
        database = db
