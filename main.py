from fastapi import FastAPI

from routers.users import router as users_router


app = FastAPI(
    title="Users API",
    description="Simple FastAPI application for managing users",
    version="1.0.0"
)

app.include_router(users_router)

@app.get("/health") 
def health()  : 
    return {"status":"health"}

@app.get("/")
def home():
    return {"message": "Welcome to the API"}