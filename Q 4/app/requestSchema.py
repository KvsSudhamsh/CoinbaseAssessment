from pydantic import BaseModel
from typing import Optional

# Request Schema
class ItemQueryParams(BaseModel):
    parent_id: str
    limit: Optional[int] = 20
    offset: Optional[int] = 0
    sort_by: Optional[str] = "created_at"
    order: Optional[str] = "desc"