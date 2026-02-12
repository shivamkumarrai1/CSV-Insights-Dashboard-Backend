from pydantic import BaseModel
from datetime import datetime
from typing import List, Any


class GenerateInsightsRequest(BaseModel):
    filename: str
    columns: List[str]
    rows: List[List[Any]]


class ReportCreate(BaseModel):
    filename: str
    summary: str


class ReportResponse(BaseModel):
    id: int
    filename: str
    summary: str
    created_at: datetime

    class Config:
        from_attributes = True
