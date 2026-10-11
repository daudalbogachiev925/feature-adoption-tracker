from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.database import Base, engine
from app.api import events, adoption

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Feature Adoption Tracker", version="1.0.0")
app.add_middleware(CORSMiddleware, allow_origins=["*"],
                   allow_methods=["*"], allow_headers=["*"])
app.include_router(events.router, prefix="/api/events", tags=["events"])
app.include_router(adoption.router, prefix="/api/adoption", tags=["adoption"])

@app.get("/health")
def health():
    return {"status": "ok"}
