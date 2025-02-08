from fastapi import FastAPI, Query, HTTPException
from database import collection
from pymongo.errors import PyMongoError
from responseSchema import ResponseSchema

app = FastAPI()

@app.get("/v1/items", response_model=ResponseSchema)
async def get_items(
    parent_id: str = Query(..., title="Parent ID"),
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    sort_by: str = Query("created_at"),
    order: str = Query("desc")
):
    # Define sorting order
    sort_order = -1 if order == "desc" else 1
    
    try:
        # Query MongoDB
        items_cursor = collection.find({"parent_id": parent_id})\
            .sort(sort_by, sort_order)\
            .skip(offset)\
            .limit(limit)

        items = list(items_cursor)

        if not items:
            raise HTTPException(status_code=404, detail="No items found for the given parent_id")

        # Format response
        formatted_items = [
            {
                "item_id": str(item["_id"]),
                "parent_id": item["parent_id"],
                "name": item.get("name", "Unknown"),
                "created_at": item.get("created_at", "")
            }
            for item in items
        ]

        total_items = collection.count_documents({"parent_id": parent_id})

        return {
            "data": formatted_items,
            "metadata": {
                "total_items": total_items,
                "limit": limit,
                "offset": offset
            }
        }
    
    except PyMongoError as e:
        raise HTTPException(status_code=500, detail="Database error: " + str(e))

