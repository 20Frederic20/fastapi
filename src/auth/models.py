from sqlalchemy import Column, String, Boolean, DateTime
from sqlalchemy.dialects.postgresql import UUID
import uuid
from datetime import datetime
from src.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String, unique=True, nullable=False)
    password = Column(String, nullable=False)
    email = Column(String)
    is_active = Column(Boolean, default=False)
    is_banned = Column(Boolean, default=False)
    is_creator = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    date_joined = Column(DateTime, default=datetime.utcnow)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    last_login = Column(DateTime)

# Base.metadata.tables["users"]

# from pydantic import BaseModel
# from uuid import uuid4
# from datetime import datetime


# class User(BaseModel): 
#     id: uuid4
#     first_name: str | None = None
#     last_name: str | None = None
#     username: str
#     password: str
#     email: str | None = None
#     is_active: bool = False
#     is_banned: bool = False
#     is_creator: bool = False
#     is_admin: bool = False
#     date_joined: datetime | None = None
#     created_at: datetime | None = None
#     updated_at: datetime | None = None
#     last_login: datetime | None = None