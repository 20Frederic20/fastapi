from fastapi import FastAPI
from auth.router import router as auth_router
from posts.router import router as posts_router
from .config import settings
from .database import engine, Base

app = FastAPI(title=settings.PROJECT_NAME)

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(auth_router, prefix="/auth", tags=["auth"])
app.include_router(posts_router, prefix="/posts", tags=["posts"])

@app.get("/")
async def root():
    return {"message": "Welcome to our FastAPI application!"}

    
if __name__ == "__main__": 
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8443, reload=True)
