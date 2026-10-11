import os
import requests
import pandas as pd
import plotly.express as px
import streamlit as st

API = os.getenv("API_URL", "http://api:8000")
st.set_page_config(page_title="Feature Adoption", layout="wide")
st.title("Feature Adoption Tracker")

@st.cache_data(ttl=15)
def fetch(path): return requests.get(f"{API}{path}").json()
@st.cache_data(ttl=15)
def post(path): return requests.post(f"{API}{path}").json()

summary = fetch("/api/adoption")
metrics = pd.DataFrame(summary["metrics"])
low = pd.DataFrame(fetch("/api/adoption/low"))

c1, c2, c3, c4 = st.columns(4)
c1.metric("Пользователей", summary["total_users"])
c2.metric("Фич", summary["total_features"])
c3.metric("Событий", summary["total_events"])
c4.metric("Низкий adoption", len(low))

if not metrics.empty:
    st.subheader("Adoption rate по фичам")
    st.plotly_chart(px.bar(metrics.sort_values("adoption_rate"),
                            x="feature", y="adoption_rate"))
    st.subheader("События по фичам")
    st.plotly_chart(px.bar(metrics.sort_values("total_events"),
                            x="feature", y="total_events"))

if not low.empty:
    st.subheader("Фичи с низким adoption")
    st.dataframe(low)

if st.button("Пересчитать паттерны"):
    r = post("/api/adoption/recompute-patterns")
    st.json(r)
    st.cache_data.clear()

st.subheader("Кластеры пользователей")
clusters = pd.DataFrame(fetch("/api/adoption/clusters"))
if not clusters.empty:
    st.dataframe(clusters)
