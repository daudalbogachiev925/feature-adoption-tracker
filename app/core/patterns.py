import numpy as np
from collections import defaultdict
from sklearn.cluster import KMeans

def user_feature_matrix(events):
    users = sorted({e.user_id for e in events})
    features = sorted({e.feature for e in events})
    f_idx = {f: i for i, f in enumerate(features)}
    u_idx = {u: i for i, u in enumerate(users)}
    m = np.zeros((len(users), len(features)), dtype=int)
    for e in events:
        m[u_idx[e.user_id], f_idx[e.feature]] = 1
    return users, features, m

def cluster_users(matrix, n_clusters=4):
    if len(matrix) < n_clusters:
        return np.zeros(len(matrix), dtype=int)
    km = KMeans(n_clusters=n_clusters, random_state=0, n_init=10).fit(matrix)
    return km.labels_
