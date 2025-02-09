from fastapi import APIRouter, HTTPException, Query
from models import Item
from typing import List
from datetime import datetime

router = APIRouter()

# Sample Data
data_store = [
    {"id": 1, "name": "BTC", "description": "Bitcoin", "created_at": str(datetime.now())},
    {"id": 2, "name": "ETH", "description": "Ethereum", "created_at": str(datetime.now())},
]

@router.get("/", response_model=List[Item])
async def get_data(limit: int = Query(10, description="Number of items to return")):
    return data_store[:limit]

@router.get("/{item_id}", response_model=Item)
async def get_item(item_id: int):
    for item in data_store:
        if item["id"] == item_id:
            return item
    raise HTTPException(status_code=404, detail="Item not found")
