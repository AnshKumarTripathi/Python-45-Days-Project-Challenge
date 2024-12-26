import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

ratings = pd.read_csv('data/u.data', sep='\t', names=['userId', 'movieId', 'rating', 'timestamp'])
movies = pd.read_csv('data/u.item', sep='|', encoding='latin-1', usecols=[0, 1], names=['movieId', 'title'])

data = pd.merge(ratings, movies, on='movieId')

user_item_matrix = data.pivot_table(index='userId', columns='title', values='rating')

user_item_matrix = user_item_matrix.fillna(0)

user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)

def get_top_n_similar_users(user_id, n=20, min_overlap=5):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).iloc[1:]
    valid_users = []
    for other_user_id in similar_users.index:
        overlap = user_item_matrix.loc[[user_id, other_user_id]].notna().sum().sum()
        if overlap >= min_overlap:
            valid_users.append(other_user_id)
        if len(valid_users) >= n:
            break
    return valid_users

def get_recommendations(user_id, n=10):
    similar_users = get_top_n_similar_users(user_id, n=20)
    user_similarities = user_similarity_df.loc[user_id, similar_users]

    similar_users_ratings = user_item_matrix.loc[similar_users]
    weighted_ratings = (similar_users_ratings.T * user_similarities).T
    recommendation_scores = weighted_ratings.sum(axis=0) / user_similarities.sum()

    user_ratings = user_item_matrix.loc[user_id]
    recommendations = recommendation_scores[user_ratings.isna()].sort_values(ascending=False).head(n)

    return recommendations

if __name__ == "__main__":
    user_id = 1
    
    user_ratings = user_item_matrix.loc[user_id]
    print("\nUser Ratings:")
    print(user_ratings[user_ratings > 0])
    
    recommendations = get_recommendations(user_id, n=10)
    print("\nRecommendations:")
    print(recommendations)
