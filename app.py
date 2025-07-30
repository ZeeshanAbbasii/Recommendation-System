import streamlit as st
import pandas as pd
import os
import pickle
from src.recommender import get_recommendations
from src.utils import load_dataset

# --- Load Models from Relative Path ---
def load_models():
    base_dir = os.path.dirname(__file__)
    model_dir = os.path.join(base_dir, "models")

    with open(os.path.join(model_dir, "svd_model.pkl"), "rb") as f:
        svd_model = pickle.load(f)

    with open(os.path.join(model_dir, "tfidf_vectorizer.pkl"), "rb") as f:
        tfidf = pickle.load(f)

    return svd_model, tfidf

# --- Streamlit UI ---
st.set_page_config(page_title="🔍 Movie Recommendation System", layout="wide")

st.title("🎬 Movie Recommendation System")

st.sidebar.header("📁 Upload Section")

uploaded_file = st.sidebar.file_uploader("Upload your dataset (CSV format)", type=["csv"])

if uploaded_file:
    try:
        df = load_dataset(uploaded_file)
        st.success("✅ Dataset loaded successfully!")

        svd_model, tfidf = load_models()

        movie_title = st.selectbox("🎞️ Select a movie title", df['title'].values)

        if st.button("🎯 Recommend Similar Movies"):
            with st.spinner("🔍 Finding recommendations..."):
                recommendations = get_recommendations(movie_title, svd_model, tfidf, df)
                st.subheader("📋 Top 10 Recommendations")
                st.table(recommendations)
    except Exception as e:
        st.error(f"❌ An error occurred: {e}")
else:
    st.info("ℹ️ Please upload a movie dataset to begin.")