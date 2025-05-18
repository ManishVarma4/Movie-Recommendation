import streamlit as st
import pickle
import pandas as pd
import requests
import os
from dotenv import load_dotenv

# Load API key from .env
load_dotenv()
api = os.getenv("TMDB_API_KEY")

def fetch_poster(movie_id):
    try:
        response = requests.get(
            f'https://api.themoviedb.org/3/movie/{movie_id}?api_key={api}&language=en-US',
            timeout=5
        )
        response.raise_for_status()
        data = response.json()
        return "http://image.tmdb.org/t/p/w500/" + data['poster_path']
    except Exception as e:
        print(f"Error fetching poster: {e}")
        return "https://via.placeholder.com/500x750?text=Poster+Unavailable"


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    rec_mov_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    recommended_movies = []
    poster = []
    for i in rec_mov_list:
        movie_id = i[0]
        recommended_movies.append(movies.iloc[movie_id]['title'])
        poster.append(fetch_poster(movie_id))
    return recommended_movies, poster

# Load data
movies_list = pickle.load(open("movies.pkl", "rb"))
movies = pd.DataFrame(movies_list)
similarity = pickle.load(open("similarity.pkl", "rb"))

# Streamlit UI
st.title('Movie Recommender System')
option = st.selectbox('Select a Movie', movies['title'].values)

if st.button('Recommend Movies'):
    recommendations, poster = recommend(option)
    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.header(recommendations[0])
        st.image(poster[0])
    with col2:
        st.header(recommendations[1])
        st.image(poster[1])
    with col3:
        st.header(recommendations[2])
        st.image(poster[2])
    with col4:
        st.header(recommendations[3])
        st.image(poster[3])
    with col5:
        st.header(recommendations[4])
        st.image(poster[4])