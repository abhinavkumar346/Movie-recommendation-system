import streamlit as st
from difflib import get_close_matches
import pickle
import requests

def fetch_poster(movie_id):
     url = "https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US".format(movie_id)
     data=requests.get(url)
     data=data.json()
     poster_path = data['poster_path']
     full_path = "https://image.tmdb.org/t/p/w500/"+poster_path
     return full_path
# Load data
movies = pickle.load(open("movies_list.pkl", "rb"))
similarity = pickle.load(open("similarity.pkl", "rb"))

movies_list = movies['title'].values

st.header("Movie Recommender System")
select_value = st.selectbox("Search or select a movie", movies_list)

from difflib import get_close_matches
def recommend(movie):
    movie = movie.strip().lower()
    titles = movies['title'].str.lower().tolist()

    matches = get_close_matches(movie, titles, n=1, cutoff=0.6)
    if not matches:
        return [], []

    movie_index = movies[movies['title'].str.lower() == matches[0]].index[0]

    distances = similarity[movie_index]
    movies_list = sorted(enumerate(distances), key=lambda x: x[1], reverse=True)

    recommended_movies = []
    recommended_posters = []

    for i in movies_list[1:6]:
        movie_id = movies.iloc[i[0]].id
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_posters.append(fetch_poster(movie_id))

    return recommended_movies, recommended_posters


# Button action
if st.button("Show Recommend"):
    movie_name,movie_poster = recommend(select_value)

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1:
        st.text(movie_name[0])
        st.image(movie_poster[0])
    with col2:
        st.text(movie_name[1])
        st.image(movie_poster[1])
    with col3:
        st.text(movie_name[2])
        st.image(movie_poster[2])
    with col4:
        st.text(movie_name[3])
        st.image(movie_poster[3])
    with col5:
        st.text(movie_name[4])
        st.image(movie_poster[4])
