from pydantic import BaseModel, EmailStr
from uuid import uuid4

class UserOut(BaseModel):
    id: int
    email: str
    username: str

    class Config:
        from_attributes = True

# ... other existing schemas ...

class UserCreate(BaseModel):
    email: str
    username: str
    password: str

class UserLogin(BaseModel):
    email: str
    password: str

class UserUpdate(BaseModel):
    username: str
    password: str

class UserDelete(BaseModel):
    email: str

class User(BaseModel):
    id: uuid4
    username: str
    email: str
    password: str
    is_active: bool
    is_creator: bool
    is_admin: bool
    