import aioredis
from fastapi import APIRouter

cache_router = APIRouter()
redis = aioredis.from_url("redis://localhost:6379")

@cache_router.get("/get/{key}")
async def get_cache(key: str):
    value = await redis.get(key)
    return {"key": key, "value": value}

@cache_router.post("/set/{key}/{value}")
async def set_cache(key: str, value: str):
    await redis.set(key, value, ex=60)  # Expires in 60 seconds
    return {"message": f"Key {key} stored successfully"}
