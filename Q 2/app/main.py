from fastapi import FastAPI
from routers import router
from auth import auth_router
from cache import cache_router

app = FastAPI()

# Include modular routers
app.include_router(router, prefix="/data")
app.include_router(auth_router, prefix="/auth")
app.include_router(cache_router, prefix="/cache")

@app.get("/")
async def root():
    return {"message": "Welcome to Backend System X"}
