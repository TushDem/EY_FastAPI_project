from fastapi import APIRouter, HTTPEception
from datetime import datetime
from app.models.request_models import AdditionRequest
from app.models.response_models import AdditionResponse
from app.services.addition_service import perform_addition
from app.utils.logger import logger

router = APIRouter()

@router.post("/add", response_model=AdditionResponse)
async def add_numbers(request:AdditionRequest):
    started_at = datetime.utcnow()
    try:
        results = perform_addition(request.payload)
        completed_at = datetime.utcnow()
        return AdditionResponse(batch_id=request.batch_id, response=results, status="complete",started_at=started_at,completed_at=completed_at)
    except Exception as e:
        logger.error(f"Error while adding numbers: {str(e)}")
        raise
    HTTPEception(status_code=500, detail="Internal Server Error")