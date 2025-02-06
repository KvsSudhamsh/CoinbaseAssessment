from pydantic import BaseModel
from typing import List

# Response Schema
class Item(BaseModel):
    item_id: str
    parent_id: str
    name: str
    created_at: str

class ResponseSchema(BaseModel):
    data: List[Item]
    metadata: dict