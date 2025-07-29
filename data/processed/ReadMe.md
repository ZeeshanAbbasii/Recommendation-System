## 📂 Processed Data Folder

This directory contains the processed data files used for training, evaluation, and recommendation generation in this project. Due to large file sizes, **these files are not uploaded to GitHub**, but are essential to reproduce the full pipeline.

### 📄 File Overview

| File Name                        | Description                                           | Size      |
|----------------------------------|-------------------------------------------------------|-----------|
| `cleaned_reviews.csv`            | Cleaned review dataset used for model training       | ~1.26 GB  |
| `cosine_similarity_50k_batched.pkl` | Precomputed cosine similarity matrix for 50k items (batched) | ~24.7 GB |
| `item_encoder.pkl`              | Fitted encoder for item (product) IDs                | ~41 KB    |
| `metadata_50k.csv`              | Filtered metadata for 50,000 items                   | ~220 MB   |
| `metadata_cleaned.csv`          | Fully cleaned product metadata                       | ~6.51 GB  |
| `user_encoder.pkl`              | Fitted encoder for user IDs                          | ~41 KB    |
| `user_item_matrix_5000.csv`     | User-item matrix used for collaborative filtering    | ~25 MB    |
| `user_item_matrix_5000.pkl`     | Binary-serialized version of the matrix              | ~200 MB   |

---

### ⚠️ Note on Availability

Due to GitHub’s file size limitations and project size (~50 GB), these files are **not hosted in the repository**.

If you would like access to these files for research, testing, or collaboration:

📧 **Contact:** [abasizishan@example.com]  
💬 Please mention your purpose briefly when requesting access.

---

### ✅ Suggested Steps

If you’ve received the dataset files via email or external link:

1. Place the files in the correct `processed/` directory.
2. Run the appropriate training or inference scripts provided in the main repo.

---

### 🛠 Future Improvement

We plan to optionally support `download_data.py` to automate downloading from a secure cloud bucket or external host in future versions.

---