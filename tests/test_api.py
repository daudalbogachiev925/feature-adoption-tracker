def test_health(client):
    assert client.get("/health").json()["status"] == "ok"

def test_add_event(client):
    r = client.post("/api/events", json={"user_id": 1, "feature": "AI"})
    assert r.status_code == 201

def test_adoption_summary(client):
    client.post("/api/events", json={"user_id": 1, "feature": "AI"})
    client.post("/api/events", json={"user_id": 2, "feature": "AI"})
    client.post("/api/events", json={"user_id": 2, "feature": "SSO"})
    r = client.get("/api/adoption")
    assert r.status_code == 200
    body = r.json()
    assert body["total_users"] == 2
    assert body["total_features"] == 2
    assert body["total_events"] == 3

def test_low_adoption(client):
    for u in range(10):
        client.post("/api/events", json={"user_id": u, "feature": "popular"})
    client.post("/api/events", json={"user_id": 11, "feature": "rare"})
    r = client.get("/api/adoption/low")
    assert r.status_code == 200
