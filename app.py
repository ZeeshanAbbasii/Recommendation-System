import streamlit as st
import pandas as pd
import pickle
import os

# Define file paths relative to current file
MODEL_DIR = os.path.join(os.path.dirname(__file__), 'models')
SVD_PATH = os.path.join(MODEL_DIR, 'svd_model.pkl')
TFIDF_PATH = os.path.join(MODEL_DIR, 'tfidf_vectorizer.pkl')

@st.cache_resource
def load_models():
    try:
        with open(SVD_PATH, 'rb') as svd_file:
            svd_model = pickle.load(svd_file)
        with open(TFIDF_PATH, 'rb') as tfidf_file:
            tfidf = pickle.load(tfidf_file)
        return svd_model, tfidf
    except FileNotFoundError:
        st.error("Model files not found. Please make sure svd_model.pkl and tfidf_vectorizer.pkl exist in the 'models/' directory.")
        st.stop()
    except Exception as e:
        st.error(f"An error occurred while loading models: {e}")
        st.stop()

def main():
    st.title("🔍 Movie Recommendation System")

    st.markdown("### Upload your dataset (CSV format)")
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        st.write("### Uploaded Data Preview:")
        st.dataframe(df.head())

        # Load models only when needed
        svd_model, tfidf = load_models()
        st.success("Models loaded successfully! 🎉")

        # Placeholder for your recommendation logic
        st.write("✅ Ready to generate recommendations...")

    else:
        st.info("📂 Please upload a dataset to begin.")

if __name__ == "__main__":
    main()