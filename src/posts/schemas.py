from pydantic import BaseModel
from uuid import uuid4
from auth.schemas import User

def PostCreate(BaseModel):
    title: str
    content: str
    published: bool = True
    user_id: USer


class Post(BaseModel):
    id: uuid4
    title: str
    content: str
    published: bool
    user_id: User


class PostUpdate(BaseModel):
    title: str
    content: str
    published: bool


class PostDelete(BaseModel):
    id: uuid4


