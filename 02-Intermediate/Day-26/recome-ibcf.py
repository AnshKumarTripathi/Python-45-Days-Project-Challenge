import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

ratings = pd.read_csv('data/u.data', sep='\t', names=['userId', 'movieId', 'rating', 'timestamp'])
movies = pd.read_csv('data/u.item', sep='|', encoding='latin-1', usecols=[0, 1], names=['movieId', 'title'])

data = pd.merge(ratings, movies, on='movieId')

user_item_matrix = data.pivot_table(index='userId', columns='title', values='rating')

user_item_matrix = user_item_matrix.fillna(0)

item_user_matrix = user_item_matrix.T

item_similarity = cosine_similarity(item_user_matrix)
item_similarity_df = pd.DataFrame(item_similarity, index=item_user_matrix.index, columns=item_user_matrix.index)

def get_top_n_similar_items(movie_title, n=5):
    similar_items = item_similarity_df[movie_title].sort_values(ascending=False).iloc[1:n+1].index
    return similar_items

def get_item_based_recommendations(user_id, movie_title, n=5):
    similar_items = get_top_n_similar_items(movie_title, n)
    similar_items_ratings = user_item_matrix[similar_items].mean(axis=1)
    
    recommendations = similar_items_ratings[user_item_matrix[movie_title].isna()].sort_values(ascending=False).head(n)
    return recommendations

if __name__ == "__main__":
    user_id = 1
    movie_title = 'Toy Story (1995)'
    recommendations = get_item_based_recommendations(user_id, movie_title)
    print(recommendations)
