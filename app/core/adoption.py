from collections import defaultdict

def adoption_metrics(events, total_users):
    by_feature_users = defaultdict(set)
    by_feature_count = defaultdict(int)
    for e in events:
        by_feature_users[e.feature].add(e.user_id)
        by_feature_count[e.feature] += 1
    result = []
    for feature, users in by_feature_users.items():
        result.append({
            "feature": feature,
            "users": len(users),
            "adoption_rate": len(users) / max(total_users, 1),
            "total_events": by_feature_count[feature],
        })
    result.sort(key=lambda x: -x["adoption_rate"])
    return result

def low_adoption_features(metrics, threshold):
    return [m for m in metrics if m["adoption_rate"] < threshold]
