from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field
from datetime import datetime
from ..core.logging import setup_logger

router = APIRouter()
logger = setup_logger()

class SpliceEntry(BaseModel):
    crew_name: str = Field(..., description="Name of the crew performing the splice")
    segment_id: str = Field(..., description="Unique identifier for the fiber segment")
    splice_type: str = Field(..., description="Type of splice performed")
    timestamp: str = Field(default_factory=lambda: datetime.now().isoformat())
    notes: str | None = Field(None, description="Additional notes about the splice")

    def validate_splice_type(self):
        valid_types = ["fusion", "mechanical", "preconnectorized"]
        if self.splice_type.lower() not in valid_types:
            raise ValueError(f"Invalid splice type. Must be one of: {', '.join(valid_types)}")

@router.post("/api/splice")
def log_splice(entry: SpliceEntry):
    try:
        entry.validate_splice_type()
        logger.info(f"Splice logged - Crew: {entry.crew_name}, Segment: {entry.segment_id}, Type: {entry.splice_type}")
        return {"status": "ok", "data": entry.dict()}
    except ValueError as e:
        logger.error(f"Invalid splice entry: {str(e)}")
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        logger.error(f"Error logging splice: {str(e)}")
        raise HTTPException(status_code=500, detail="Internal server error")
