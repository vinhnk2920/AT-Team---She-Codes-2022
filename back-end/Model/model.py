from peewee import *
from Model.base import BaseModel


class LoginInformation(BaseModel):
    id = IntegerField()
    username = CharField()
    password = CharField()

    class Meta:
        table_name = "login_information"


class MemberOfProject(BaseModel):
    id = IntegerField()
    user_id = IntegerField()
    project_id = IntegerField()
    created_by = IntegerField()

    class Meta:
        table_name = "member_of_project"


class Quote(BaseModel):
    id = IntegerField()
    content = CharField()
    author = CharField()

    class Meta:
        table_name = "quotes"


class Project(BaseModel):
    id = IntegerField()
    name = CharField()
    avatar = CharField()
    description = CharField()

    class Meta:
        table_name = "projects"
