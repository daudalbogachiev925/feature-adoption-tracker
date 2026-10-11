from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.models import FeatureEvent
from app.schemas import AdoptionSummary, AdoptionMetric
from app.core.adoption import adoption_metrics, low_adoption_features
from app.core.patterns import user_feature_matrix, cluster_users
from app.config import settings

router = APIRouter()

@router.get("", response_model=AdoptionSummary)
def summary(db: Session = Depends(get_db)):
    events = db.query(FeatureEvent).all()
    total_users = len({e.user_id for e in events})
    metrics = adoption_metrics(events, total_users)
    return AdoptionSummary(total_users=total_users,
                            metrics=[AdoptionMetric(**m) for m in metrics])

@router.get("/low")
def low(db: Session = Depends(get_db)):
    events = db.query(FeatureEvent).all()
    total_users = len({e.user_id for e in events})
    metrics = adoption_metrics(events, total_users)
    return low_adoption_features(metrics, settings.LOW_ADOPTION_THRESHOLD)

@router.get("/patterns")
def patterns(db: Session = Depends(get_db)):
    events = db.query(FeatureEvent).all()
    if len(events) < 5:
        return {"error": "not enough events"}
    users, features, matrix = user_feature_matrix(events)
    labels = cluster_users(matrix, n_clusters=min(4, len(users)))
    return {
        "features": features,
        "users": [{"user_id": int(u), "cluster": int(l)}
                  for u, l in zip(users, labels)],
    }
