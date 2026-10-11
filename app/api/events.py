from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from datetime import datetime
from app.database import get_db
from app.models import FeatureEvent
from app.schemas import EventCreate, EventRead

router = APIRouter()

@router.post("", response_model=EventRead, status_code=201)
def add(payload: EventCreate, db: Session = Depends(get_db)):
    data = payload.model_dump()
    if data.get("used_at") is None:
        data["used_at"] = datetime.utcnow()
    e = FeatureEvent(**data)
    db.add(e)
    db.commit()
    db.refresh(e)
    return e

@router.post("/batch", status_code=201)
def add_batch(payloads: List[EventCreate], db: Session = Depends(get_db)):
    for p in payloads:
        data = p.model_dump()
        if data.get("used_at") is None:
            data["used_at"] = datetime.utcnow()
        db.add(FeatureEvent(**data))
    db.commit()
    return {"inserted": len(payloads)}

@router.get("", response_model=List[EventRead])
def list_events(db: Session = Depends(get_db), limit: int = 1000):
    return db.query(FeatureEvent).limit(limit).all()
