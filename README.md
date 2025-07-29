📦 E-Commerce Recommendation System

🧠 Project Description

This project focuses on building a hybrid recommendation system for an e-commerce platform using both collaborative filtering and content-based filtering techniques. The goal is to enhance user experience by suggesting personalized product recommendations based on past user interactions and product metadata.

The system is designed using a subset of the Amazon Electronics Review dataset and demonstrates how modern recommendation algorithms can be built, evaluated, and optimized for large-scale e-commerce platforms.

⸻

🎯 What This Project Does
	•	Cleans and preprocesses raw user-product interaction and metadata.
	•	Analyzes data trends such as user behavior, product popularity, and rating patterns.
	•	Implements two core recommendation strategies:
	•	Content-Based Filtering using product metadata (titles, categories, descriptions).
	•	Collaborative Filtering using matrix factorization (SVD).
	•	Combines both techniques into a hybrid model for improved recommendations.
	•	Evaluates models using metrics like RMSE, Precision@K, Recall@K, and MAP (Mean Average Precision).
	•	Generates product recommendations for individual users and visualizes key insights.

⸻

🛠️ Technologies & Techniques Used
	•	Programming Language: Python
	•	Libraries:
	•	Data Handling: pandas, numpy
	•	Visualization: matplotlib, seaborn
	•	NLP & Similarity: scikit-learn (TF-IDF, Cosine Similarity)
	•	Collaborative Filtering: Surprise (SVD)
	•	Serialization: pickle
	•	Recommendation Techniques:
	•	Content-Based Filtering (TF-IDF + Cosine Similarity)
	•	Collaborative Filtering (Matrix Factorization using SVD)
	•	Hybrid Recommender (Weighted combination of both)

⸻

📊 Results Achieved
	•	Built a scalable recommender system capable of providing relevant suggestions to users.
	•	Achieved acceptable performance on RMSE and ranking metrics using only 50k user-product interactions.
	•	Demonstrated that combining collaborative and content-based approaches improved recommendation quality.
	•	Delivered real-time recommendations using precomputed similarity and trained models.

⸻

📦 Dataset Used
	•	Dataset: Amazon Electronics Review dataset
	•	Files:
	•	Electronics_5.json: Contains user-product reviews and ratings.
	•	meta_Electronics.json: Contains metadata such as product titles, categories, and descriptions.

Note: These files are not included in the repository due to their large size (~50GB total).
For your own experimentation, you can download the dataset from Amazon Reviews - SNAP (Electronics category).

⸻

⚠️ Note on Dataset Size

While the full dataset includes 1.1 million+ interactions, this project was built using a 50,000-record subset to ensure fast prototyping, training, and evaluation without compromising learning outcomes. This approach significantly reduces compute time while maintaining meaningful patterns for model training and analysis.
