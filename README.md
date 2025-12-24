# Learning Recommendation System 📚🤖

An end-to-end **learning recommendation system** that suggests the next relevant courses
to learners based on historical interaction data from a MOOC platform.

This project demonstrates a complete pipeline from raw interaction logs and feature engineering
to sequence-based modeling, hybrid recommendation strategies, and deployment using Streamlit.

---

## Problem Statement

Online learning platforms host thousands of courses, making it difficult for learners
to identify the next most relevant learning item.

Traditional recommendation methods often:
- Ignore temporal learning behavior
- Struggle with cold-start users
- Over-rely on globally popular content

---

## Solution Overview

This project builds a production-style recommender system that:
- Learns from user interaction sequences
- Handles cold-start and sparse users
- Uses hybrid and two-stage ranking strategies
- Demonstrates recommendations via a web application

---

## System Pipeline

Data Ingestion (XuetangX MOOC Dataset)  
↓  
Data Cleaning & Feature Engineering  
↓  
Interaction Strength Aggregation  
↓  
Temporal Train / Validation / Test Split  
↓  
Baseline Models (Most Popular, Collaborative Filtering)  
↓  
Sequence Model (GRU4Rec-style)  
↓  
Hybrid Recommendation Strategy  
↓  
Candidate Generation  
↓  
Ranking with Sequence Model  
↓  
Evaluation (Precision, Recall, NDCG, MRR)  
↓  
Streamlit Web Application  

---

## Dataset

- **Source:** XuetangX MOOC Dataset (Kaggle)
-  https://www.kaggle.com/datasets/anasnofal/mooc-data-xuetangx
- **Type:** Implicit feedback (clicks, video views, problem solving, discussions)

Each interaction consists of:
- Learner identifier
- Course identifier
- Timestamp
- Fine-grained behavioral signals (`action_*` columns)

---

## Feature Engineering

User behavior was converted into a single **interaction strength** score using weighted aggregation:

- Browsing actions → low intent  
- Video interactions → medium intent  
- Problem-solving actions → high intent  
- Social interactions → engagement signal  

Additional preprocessing steps:
- Log normalization of interaction strength
- Timestamp conversion to datetime
- Chronological sorting per user
- Encoding of users and items

---

## Temporal Data Split

A **per-user temporal split** was applied to avoid data leakage:

- Training set → earliest interactions  
- Validation set → intermediate interactions  
- Test set → most recent interactions  

Users with extremely short histories were excluded from evaluation.

---

## Models Implemented

### Most Popular Baseline
- Recommends globally popular courses
- Strong fallback for cold-start users
- No personalization

---

### Collaborative Filtering (ALS)
- Matrix factorization on implicit feedback
- Learns latent user–item representations
- Performs poorly under high sparsity

---

### Sequence Model (GRU4Rec-style)
- Models ordered user interaction sequences
- Predicts the next learning item
- Captures short-term learning intent
- **Best performing model in this project**

---

### Hybrid Recommendation Model

A rule-based hybrid strategy:
- No history → Most Popular  
- Short history → Popular + Sequence  
- Sufficient history → Sequence only  

Improves robustness across diverse learners.

---

## Candidate Generation and Ranking

To simulate real-world recommender systems, a **two-stage pipeline** was implemented.

Candidate Generation  
↓  
- Top globally popular items  
- User’s recent interaction history  
↓  
Candidate Pool (Top-100)  
↓  
Sequence-Based Ranking  
↓  
Final Top-K Recommendations  

**Candidate Recall@100 ≈ 55%**

---

## Evaluation Metrics

Models were evaluated using ranking-based metrics:
- Precision@K
- Recall@K
- NDCG@K
- Mean Reciprocal Rank (MRR)

---

## Results Summary (K = 10)

| Model | Precision | Recall | NDCG | MRR |
|------|----------|--------|------|-----|
| Most Popular | 0.0157 | 0.1391 | 0.0688 | 0.0498 |
| Collaborative Filtering | 0.0008 | 0.0054 | 0.0030 | 0.0027 |
| Sequence (GRU) | **0.0413** | **0.3576** | **0.2065** | **0.1676** |
| Hybrid | 0.0254 | 0.1985 | 0.1134 | 0.0947 |

---

## Error Analysis

Qualitative error inspection revealed:
- Short interaction histories reduce personalization
- Topic shifts are difficult to predict
- Candidate recall limits downstream ranking

These insights motivated the hybrid and two-stage design.

---

## Cold-Start and Novelty Analysis

### Cold-Start Handling
Cold-start users are explicitly handled using popularity-based fallback logic.
The hybrid model adapts recommendations based on history length.

### Novelty
Novelty was analyzed qualitatively:
- Popular model → low novelty
- Sequence and hybrid models → reduced popularity bias

---

## Streamlit Web Application

A Streamlit-based web app demonstrates real-time recommendations.

### Features
- User ID input
- Top-K selection
- Display of recent user history
- Hybrid recommendation logic
- Cold-start detection

This validates the end-to-end pipeline from data to deployment.
