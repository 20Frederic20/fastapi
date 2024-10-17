from sqlalchemy.orm import Session
from . import schemas
from .models import User

def create_user(db: Session, user: schemas.UserCreate):
    db_user = User(email=user.email, username=user.username, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def update_user(db: Session, user_id: int, user: schemas.UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db_user.username = user.username
        db_user.password = user.password
        db.commit()
        db.refresh(db_user)
    return db_user

def delete_user(db: Session, email: str):
    db_user = db.query(User).filter(User.email == email).first()
    if db_user:
        db.delete(db_user)
        db.commit()
    return db_user

def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

def get_user_by_email(db: Session, email: str):
    return db.query(User).filter(User.email == email).first()

def get_user_by_username(db: Session, username: str):
    return db.query(User).filter(User.username == username).first()

