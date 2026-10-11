from app.core.patterns import user_feature_matrix, cluster_users, cluster_summary

class E:
    def __init__(self, uid, feat):
        self.user_id = uid
        self.feature = feat

def test_user_feature_matrix():
    events = [E(1, "A"), E(1, "B"), E(2, "A"), E(3, "C")]
    users, features, matrix = user_feature_matrix(events)
    assert len(users) == 3
    assert len(features) == 3
    assert matrix.shape == (3, 3)

def test_cluster_summary():
    events = [E(i, f) for i in range(20) for f in ["A", "B", "C"]]
    users, features, matrix = user_feature_matrix(events)
    labels = cluster_users(matrix, n_clusters=2)
    summary = cluster_summary(users, features, matrix, labels)
    assert len(summary) == 2
