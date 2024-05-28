from pydantic import BaseModel
from typing import List
from datetime import datetime

class AdditionResponse(BaseModel):
    batch_id: str
    response: List[int]
    status: str
    started_at: datetime
    completed_at: datetime