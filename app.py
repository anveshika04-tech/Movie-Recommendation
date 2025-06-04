import numpy as np
import pandas as pd
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the movie dataset
movies_data = pd.read_csv('movies.csv')

# Preprocessing
selected_features = ['genres', 'keywords', 'tagline', 'cast', 'director']
for feature in selected_features:
    movies_data[feature] = movies_data[feature].fillna('')

combined_features = movies_data['genres'] + ' ' + movies_data['keywords'] + ' ' + movies_data['tagline'] + ' ' + movies_data['cast'] + ' ' + movies_data['director']

# Vectorizing
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(feature_vectors)

# Route for home page
@app.route('/')
def index():
    return render_template('index.html')

# Route to get recommendations
@app.route('/recommend', methods=['POST'])
def recommend():
    movie_name = request.form['movie_name']  # Get the movie name from the form

    # Find the closest match in movie titles
    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    if not find_close_match:
        return render_template('recommendations.html', movie_name=movie_name, recommendations=[], error="Movie not found.")

    close_match = find_close_match[0]

    # Find the index of the movie
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

    # Get similarity scores for that movie
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    # Display top 30 movies
    recommended_movies = []
    for i, movie in enumerate(sorted_similar_movies):
        index = movie[0]
        title_from_index = movies_data.iloc[index]['title']
        if i < 30:  # Limit to 30 movies
            recommended_movies.append(title_from_index)

    return render_template('recommendations.html', movie_name=close_match, recommendations=recommended_movies)

if __name__ == '__main__':
    app.run(debug=True)
