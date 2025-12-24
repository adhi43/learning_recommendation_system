📚 Learning Recommendation System (MOOC – XuetangX)

An end-to-end learning recommendation system that suggests the next relevant courses to learners based on historical interaction data.
This project was built as part of Challenge 3: Learning Recommendation System and covers the full pipeline from data preprocessing to model deployment using Streamlit.

🚀 Project Overview

Online learning platforms generate large volumes of user interaction data. The goal of this project is to leverage that data to:

Recommend next learning items (courses)

Handle cold-start users

Model temporal learning behavior

Evaluate recommendations using ranking metrics

Demonstrate the system via a Streamlit web app

The project implements and compares:

Popularity-based baseline

Collaborative Filtering (ALS)

Sequence-based model (GRU4Rec-style)

Hybrid recommendation strategy

Candidate generation + ranking pipeline

📂 Dataset

Source: XuetangX MOOC Dataset (Kaggle)

Type: Implicit feedback (clicks, video actions, problem solving, etc.)

Key Fields:

username – learner ID

course_id – course identifier

timestamp – interaction time

Multiple action_* columns representing user behavior

Raw behavioral signals were aggregated into a single interaction strength score using weighted action grouping and log normalization.

🧠 Feature Engineering

Weighted aggregation of actions:

Browsing (low intent)

Video interactions (medium intent)

Problem solving (high intent)

Social actions (engagement signal)

Log normalization to handle long-tailed distributions

Temporal sorting per user

Conversion of timestamps to datetime format

User and item encoding for modeling

🔀 Temporal Data Split

A per-user temporal split was used to avoid data leakage:

70% → Train

15% → Validation

15% → Test

Users with extremely short histories were excluded from evaluation to ensure stability.

🤖 Models Implemented
1️⃣ Most Popular Baseline

Recommends globally popular courses

Strong baseline for cold-start users

No personalization

2️⃣ Collaborative Filtering (ALS)

Matrix factorization using implicit feedback

Learns latent user and item embeddings

Struggles due to high sparsity and short user histories

3️⃣ Sequence Model (GRU4Rec-style)

Models user interactions as ordered sequences

Uses GRU to predict the next course

Captures short-term learning intent

Best performing model overall

4️⃣ Hybrid Model

Dynamic strategy based on user history length:

No history → Most Popular

Short history → Popular + Sequence

Sufficient history → Sequence only

Improves robustness across cold-start and active users.

⚙️ Candidate Generation & Ranking Pipeline

A two-stage recommendation architecture was implemented:

Candidate Generation

Top popular items

User’s recent interaction history

Fixed candidate pool size (Top-100)

Candidate Recall@100: ~55%

Ranking

Sequence model re-ranks candidates

Produces final Top-K recommendations

This design mirrors real-world production recommender systems.

📊 Evaluation Metrics

All models were evaluated using ranking-based metrics:

Precision@K

Recall@K

NDCG@K

MRR (Mean Reciprocal Rank)

📈 Model Performance Summary (K = 10)
Model	Precision	Recall	NDCG	MRR
Most Popular	0.0157	0.1391	0.0688	0.0498
Collaborative Filtering	0.0008	0.0054	0.0030	0.0027
Sequence (GRU)	0.0413	0.3576	0.2065	0.1676
Hybrid	0.0254	0.1985	0.1134	0.0947
🔍 Error Analysis

Qualitative error analysis was conducted by inspecting:

User history

Recommended items

Ground-truth test items

Key failure patterns:

Short histories reduce personalization

Topic shifts are difficult to predict

Candidate recall limits ranking effectiveness

These insights guided the hybrid and candidate-generation strategies.

❄️ Cold-Start & Novelty Analysis
Cold-Start

Explicitly handled using Most Popular fallback

Hybrid model adapts to history length

Cold-start logic integrated into Streamlit app

Novelty

Not measured with a formal metric

Qualitatively observed:

Popular model → low novelty

Sequence & Hybrid → more personalized, less popularity bias

🌐 Streamlit Web Application

A Streamlit app was built to demonstrate real-time recommendations.

Features:

User ID input

Top-K selection

Displays recent history

Generates recommendations using hybrid logic

Handles cold-start users explicitly

This validates the end-to-end pipeline from preprocessing to inference.

```bash

pip install -r requirements.txt

streamlit run app/streamlit\_app.py



