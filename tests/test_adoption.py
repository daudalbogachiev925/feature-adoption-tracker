from app.core.adoption import adoption_metrics, low_adoption_features

class E:
    def __init__(self, uid, feat):
        self.user_id = uid
        self.feature = feat

def test_adoption_rate():
    events = [E(1, "A"), E(2, "A"), E(3, "B"), E(1, "A")]
    m = adoption_metrics(events, total_users=3)
    feat_a = next(x for x in m if x["feature"] == "A")
    assert feat_a["users"] == 2
    assert feat_a["adoption_rate"] == round(2/3, 4)
    assert feat_a["total_events"] == 3

def test_low_adoption():
    metrics = [{"feature": "A", "adoption_rate": 0.5},
               {"feature": "B", "adoption_rate": 0.05}]
    low = low_adoption_features(metrics, 0.2)
    assert len(low) == 1
    assert low[0]["feature"] == "B"
