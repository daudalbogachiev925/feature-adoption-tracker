from datetime import datetime
from typing import Optional, List, Dict
from pydantic import BaseModel

class EventCreate(BaseModel):
    user_id: int
    feature: str
    used_at: Optional[datetime] = None

class EventRead(EventCreate):
    id: int
    class Config:
        from_attributes = True

class AdoptionMetric(BaseModel):
    feature: str
    users: int
    adoption_rate: float
    total_events: int

class AdoptionSummary(BaseModel):
    total_users: int
    metrics: List[AdoptionMetric]

class UserPattern(BaseModel):
    user_id: int
    features: List[str]
    cluster: int
