import streamlit as st
import pandas as pd
import pickle
import os

# Set a safe writable config path for Streamlit (required in Hugging Face Spaces)
os.environ["STREAMLIT_HOME"] = os.getcwd()
os.environ["XDG_CONFIG_HOME"] = os.path.join(os.getcwd(), ".config")
os.makedirs(os.environ["XDG_CONFIG_HOME"], exist_ok=True)
# Load your pre-trained model and vectorizer
@st.cache_resource
def load_model():
    with open("models/svd_model.pkl", "rb") as f:
        svd_model = pickle.load(f)
    with open("models/tfidf_vectorizer.pkl", "rb") as f:
        tfidf = pickle.load(f)
    return svd_model, tfidf

svd_model, tfidf = load_model()

st.title("📦 Product Recommendation System")

# Upload CSV
uploaded_file = st.file_uploader("Upload your dataset (CSV with user and item info)", type="csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("📊 Preview of uploaded data:", df.head())

    # Let user select a user_id to get recommendations for
    user_ids = df['user_id'].unique()
    selected_user = st.selectbox("Select user ID for recommendation:", user_ids)

    # Generate recommendations (dummy logic — replace with your real logic)
    st.subheader("🔍 Recommended Items:")
    recommended_items = df['item_id'].sample(5).tolist()  # Replace this with model.predict()
    for item in recommended_items:
        st.write(f"⭐ {item}")