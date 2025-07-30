import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def get_recommendations(title, svd_model, tfidf, df):
    title_index = df[df['title'] == title].index[0]
    movie_description_vector = tfidf.transform([df.loc[title_index, 'overview']])
    sim_scores = cosine_similarity(movie_description_vector, tfidf.transform(df['overview'])).flatten()
    sim_scores_indices = sim_scores.argsort()[-11:][::-1]

    recommended_movies = df.iloc[sim_scores_indices][['title', 'overview']].reset_index(drop=True)
    recommended_movies = recommended_movies[recommended_movies['title'] != title].head(10)
    return recommended_movies