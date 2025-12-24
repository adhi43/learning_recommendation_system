import streamlit as st
import pandas as pd
import numpy as np
from collections import defaultdict
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

# -----------------------------
# Load data
# -----------------------------
train_df = pd.read_csv(r"data\processed\test.csv")

val_df   = pd.read_csv(r"data\processed\val.csv")
test_df  = pd.read_csv(r"data\processed\test.csv")

# -----------------------------
# Load model
# -----------------------------
model = load_model(r"models\gru_model.keras")
max_len = 20

# -----------------------------
# Build user histories
# -----------------------------
user_histories = defaultdict(list)

for row in train_df.sort_values("ts_ms").itertuples():
    user_histories[row.user_idx].append(row.item_idx)

for row in val_df.sort_values("ts_ms").itertuples():
    user_histories[row.user_idx].append(row.item_idx)

# -----------------------------
# Popular items (for cold-start)
# -----------------------------
popular_items = (
    train_df.groupby("item_idx")["interaction_strength"]
    .sum()
    .sort_values(ascending=False)
    .index
    .tolist()
)

# -----------------------------
# Recommendation functions
# -----------------------------
def recommend_most_popular(k=5):
    return popular_items[:k]

def recommend_sequence(history, k=5):
    padded = pad_sequences([history], maxlen=max_len, padding="pre")
    scores = model.predict(padded, verbose=0)[0]
    return np.argsort(scores)[-k:][::-1]

def hybrid_recommend(user_idx, k=5):
    history = user_histories.get(user_idx, [])

    if len(history) == 0:
        return recommend_most_popular(k)

    return recommend_sequence(history, k)

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📚 Learning Recommendation System")
st.write("Hybrid recommender using popularity + sequence modeling")

user_idx = st.number_input(
    "Enter user index",
    min_value=0,
    max_value=int(train_df.user_idx.max()),
    step=1
)

k = st.slider("Number of recommendations", 1, 10, 5)

if st.button("Recommend"):
    history = user_histories.get(user_idx, [])

    st.subheader("User History")
    if history:
        st.write(history[-10:])
    else:
        st.write("Cold-start user (no history)")

    recs = hybrid_recommend(user_idx, k)

    st.subheader("Recommended Courses")
    for i, item in enumerate(recs, 1):
        st.write(f"{i}. Course ID: {item}")
