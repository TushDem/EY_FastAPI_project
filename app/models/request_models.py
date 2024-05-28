from pydantic import BaseModel, conlist
from typing import List

class   AdditionRequest(BaseModel):
    batch_id: str
    payload: List[conlist(int, min_items=2)]