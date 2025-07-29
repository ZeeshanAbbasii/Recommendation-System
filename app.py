import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics.pairwise import cosine_similarity

# Load model files
@st.cache_resource
def load_models():
    try:
        with open("models/svd_model.pkl", "rb") as svd_file:
            svd_model = pickle.load(svd_file)
        with open("models/tfidf_vectorizer.pkl", "rb") as tfidf_file:
            tfidf = pickle.load(tfidf_file)
        return svd_model, tfidf
    except FileNotFoundError:
        st.error("Model files not found. Please make sure svd_model.pkl and tfidf_vectorizer.pkl are in the models/ directory.")
        return None, None

svd_model, tfidf = load_models()

# Streamlit UI
st.title("🔍 Movie Recommendation System")

uploaded_file = st.file_uploader("Upload your dataset (CSV format)", type=["csv"])

if uploaded_file is not None:
    try:
        data = pd.read_csv(uploaded_file)
        st.success("✅ Dataset uploaded successfully!")
        st.write(data.head())

        movie_list = data['title'].tolist()
        selected_movie = st.selectbox("Choose a movie:", movie_list)

        if st.button("Recommend"):
            if svd_model is not None and tfidf is not None:
                try:
                    movie_idx = data[data['title'] == selected_movie].index[0]
                    movie_vec = svd_model.transform(tfidf.transform([selected_movie]))
                    similarities = cosine_similarity(movie_vec, svd_model.transform(tfidf.transform(data['title'])))
                    top_indices = similarities[0].argsort()[::-1][1:6]
                    recommendations = data.iloc[top_indices]['title'].tolist()
                    st.subheader("📽️ Top 5 Recommendations:")
                    for i, rec in enumerate(recommendations, start=1):
                        st.write(f"{i}. {rec}")
                except Exception as e:
                    st.error(f"Error during recommendation: {e}")
            else:
                st.warning("⚠️ Model not loaded.")
    except Exception as e:
        st.error(f"Could not read file: {e}")
else:
    st.info("📂 Please upload a dataset to begin.")