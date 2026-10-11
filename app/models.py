from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.sql import func
from app.database import Base

class FeatureEvent(Base):
    __tablename__ = "feature_events"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, index=True, nullable=False)
    feature = Column(String, index=True, nullable=False)
    used_at = Column(DateTime, server_default=func.now(), index=True)
    created_at = Column(DateTime, server_default=func.now())
