from fastapi import APIRouter
from datetime import datetime

router = APIRouter()

@router.get("/health")
async def health_check():
    """
    Check if the API is running and responsive.
    """
    return {
        "status": "healthy",
        "service": "xavier-api",
        "timestamp": datetime.utcnow().isoformat()
    }
