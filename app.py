import streamlit as st
import pickle
import pandas as pd
import requests

# Function to fetch movie poster from TMDB API
def fetch_poster(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=5463d2bfe728554a3fc6566da5293ddd&language=en-US')
    data = response.json()
    poster_path = data['poster_path']
    return f"https://image.tmdb.org/t/p/w500/{poster_path}"

# Function to fetch movie details from TMDB API
def fetch_movie_details(movie_id):
    response = requests.get(f'https://api.themoviedb.org/3/movie/{movie_id}?api_key=5463d2bfe728554a3fc6566da5293ddd&language=en-US')
    data = response.json()
    return {
        'title': data['title'],
        'overview': data['overview'],
        'genres': [genre['name'] for genre in data['genres']],
        'rating': data['vote_average'],
        'poster_path': fetch_poster(movie_id)
    }

# Function to recommend movies based on similarity
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:11]  # Fetching 10 movies

    recommended_movies = []
    recommended_movies_details = []
    for i in movies_list:
        movie_id = movies.iloc[i[0]].movie_id
        details = fetch_movie_details(movie_id)
        recommended_movies.append(details['title'])
        recommended_movies_details.append(details)
    return recommended_movies, recommended_movies_details

# Load movie data and similarity matrix
movies_dict = pickle.load(open('movie_dic.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# Streamlit UI setup
st.title('🎬 Movie Recommendation System')

# Search bar to select a movie
selected_movie_name = st.selectbox('Select a movie to get recommendations', movies['title'].values)

# Button to get recommendations
if st.button('Recommend'):
    names, details = recommend(selected_movie_name)
    st.subheader("Recommended Movies:")

    for i in range(5):
        with st.expander(details[i]['title']):
            st.image(details[i]['poster_path'], width=150)  # Adjust the width to make posters smaller
            st.write(f"**Rating:** {details[i]['rating']}/10")
            st.write(f"**Genres:** {', '.join(details[i]['genres'])}")
            st.write(f"**Overview:** {details[i]['overview']}")

# Adding a footer
st.markdown(
    """
    <style>
    .footer {
        position: fixed;
        left: 0;
        bottom: 0;
        width: 100%;
        background-color: #f1f1f1;
        color: black;
        text-align: center;
        padding: 10px;
    }
    </style>
    <div class="footer">
        <p>Developed with ❤️ by Shreya Verma</p>
    </div>
    """, unsafe_allow_html=True
)

# Adding a sidebar for additional features
st.sidebar.title("About")
st.sidebar.info(
    """
    This is a movie recommendation system built using Streamlit and TMDB API.
    You can select a movie from the dropdown to get top 10 similar movie recommendations along with their posters and details.
    """
)
st.sidebar.markdown("## Features")
st.sidebar.markdown("- Select a movie from the dropdown")
st.sidebar.markdown("- Get top 5 similar movie recommendations")
st.sidebar.markdown("- View movie posters, ratings, genres, and overviews")
