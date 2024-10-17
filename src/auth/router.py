from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from auth import schemas, service
from database import get_db

router = APIRouter()

@router.post("/register", response_model=schemas.UserOut)
def register(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = service.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return service.create_user(db=db, user=user)

# @router.post("/login")
# def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
#     user = service.authenticate_user(db, form_data.username, form_data.password)
#     if not user:
#         raise HTTPException(
#             status_code=status.HTTP_401_UNAUTHORIZED,
#             detail="Incorrect username or password",
#             headers={"WWW-Authenticate": "Bearer"},
#         )
#     access_token = service.create_access_token(data={"sub": user.email})
#     return {"access_token": access_token, "token_type": "bearer"}

# @router.put("/users/{user_id}/posts/{post_id}", response_model=PostResponse)
# async def update_user_post(
#     update_data: PostUpdate,  
#     post: dict[str, Any] = Depends(valid_owned_post),
# ):
#     updated_post = await service.update(id=post["id"], data=update_data)
#     return updated_post
