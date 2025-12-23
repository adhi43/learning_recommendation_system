\# 📚 Learning Recommendation System



Hybrid recommendation system that suggests next learning items based on user interaction data.



\## 🔍 Features

\- Popularity-based recommendations (cold-start)

\- Sequence-based model (GRU4Rec-style)

\- Hybrid candidate generation + ranking pipeline

\- Ranking metrics (Precision@K, Recall@K, NDCG, MRR)

\- Streamlit web application



\## 📊 Dataset

XuetangX MOOC dataset (implicit feedback, anonymized).



\## 🧠 Models

\- Most Popular (baseline)

\- Collaborative Filtering (Implicit ALS)

\- Sequence Model (GRU)

\- Hybrid recommender



\## 🚀 Run the App



```bash

pip install -r requirements.txt

streamlit run app/streamlit\_app.py



