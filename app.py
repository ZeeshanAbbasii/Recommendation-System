import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load SVD model and TF-IDF vectorizer from the models directory
@st.cache_resource
def load_models():
    try:
        with open("models/svd_model.pkl", "rb") as svd_file:
            svd_model = pickle.load(svd_file)
        with open("models/tfidf_vectorizer.pkl", "rb") as tfidf_file:
            tfidf = pickle.load(tfidf_file)
        return svd_model, tfidf
    except FileNotFoundError:
        st.error("❌ Model files not found. Please ensure svd_model.pkl and tfidf_vectorizer.pkl are present in the 'models/' directory.")
        return None, None

# Load models
svd_model, tfidf = load_models()

# App UI
st.title("🎬 Movie Recommendation System")
st.markdown("Upload a **movie dataset CSV** (must have a `title` column):")

uploaded_file = st.file_uploader("Upload CSV", type="csv")

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        st.success("✅ Dataset uploaded successfully.")
        st.write("Preview of the dataset:", data.head())

        if 'title' not in data.columns:
            st.error("❌ The uploaded CSV must have a `title` column.")
        else:
            movie_titles = data['title'].dropna().tolist()
            selected_movie = st.selectbox("🎥 Choose a movie:", movie_titles)

            if st.button("🎯 Recommend Similar Movies"):
                if svd_model is not None and tfidf is not None:
                    try:
                        # Transform selected movie to vector space
                        movie_vec = svd_model.transform(tfidf.transform([selected_movie]))
                        # Transform all movie titles
                        all_vecs = svd_model.transform(tfidf.transform(data['title'].fillna("")))
                        # Compute cosine similarity
                        similarities = cosine_similarity(movie_vec, all_vecs)
                        top_indices = similarities[0].argsort()[::-1][1:6]  # Exclude the selected movie
                        recommendations = data.iloc[top_indices]['title'].tolist()

                        st.subheader("📽️ Top 5 Recommendations:")
                        for idx, movie in enumerate(recommendations, 1):
                            st.write(f"{idx}. {movie}")
                    except Exception as e:
                        st.error(f"❌ Recommendation error: {e}")
                else:
                    st.warning("⚠️ Model files not loaded.")
    except Exception as e:
        st.error(f"❌ Failed to read CSV file: {e}")
else:
    st.info("📂 Please upload a dataset to begin.")