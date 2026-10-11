import random
from datetime import datetime
from app.database import SessionLocal
from app.models import FeatureEvent

FEATURES = ["AI Search", "Mobile App", "SSO", "API", "Slack",
            "Export", "Webhooks", "Dashboard"]

def seed(n_users=500, events_per_user=15):
    db = SessionLocal()
    try:
        for u in range(n_users):
            n = random.randint(5, events_per_user)
            for _ in range(n):
                db.add(FeatureEvent(
                    user_id=u,
                    feature=random.choice(FEATURES),
                    used_at=datetime.utcnow(),
                ))
        db.commit()
        print(f"Seeded {n_users} users")
    finally:
        db.close()

if __name__ == "__main__":
    seed()
