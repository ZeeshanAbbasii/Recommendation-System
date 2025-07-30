import pickle
import os

def load_models():
    base_path = "models"
    svd_path = os.path.join(base_path, "svd_model.pkl")
    tfidf_path = os.path.join(base_path, "tfidf.pkl")

    with open(svd_path, 'rb') as svd_file:
        svd_model = pickle.load(svd_file)
    with open(tfidf_path, 'rb') as tfidf_file:
        tfidf = pickle.load(tfidf_file)

    return svd_model, tfidf