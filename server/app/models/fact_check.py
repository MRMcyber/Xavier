from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class ClaimResult(BaseModel):
    claim: str
    verdict: str
    explanation: str
    source_links: List[str]

class FactCheckResponse(BaseModel):
    job_id: str
    status: str
    
class FactCheckHistory(BaseModel):
    id: str
    claim: str
    verdict: str
    explanation: str
    source_links: List[str]
    created_at: datetime
    
class SearchQuery(BaseModel):
    query: str
