import pickle
import streamlit as st
import requests

# -------------------------------
# Load data
# -------------------------------
movies = pickle.load(open('movie_list.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

movies = movies.reset_index(drop=True)


# -------------------------------
# Fetch poster from TMDB
# -------------------------------
def fetch_poster(movie_id):
    try:
        url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
        data = requests.get(url, timeout=5).json()

        if data.get('poster_path'):
            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

    except:
        pass

    return "https://via.placeholder.com/500x750?text=No+Image"


# -------------------------------
# Improved Recommendation Function
# -------------------------------
def recommend(movie):
    recommended_movie_names = []
    recommended_movie_posters = []

    movie = movie.lower()

    # case-insensitive match
    matches = movies[movies['title'].str.lower() == movie]

    if matches.empty:
        return [], []

    index = matches.index[0]

    distances = list(enumerate(similarity[index]))

    # sort by similarity score
    distances = sorted(distances, key=lambda x: x[1], reverse=True)

    count = 0

    for i in distances[1:20]:   # take more candidates first
        if i[1] > 0.05:         # filter weak similarity
            movie_id = movies.iloc[i[0]].movie_id
            recommended_movie_names.append(movies.iloc[i[0]].title)
            recommended_movie_posters.append(fetch_poster(movie_id))
            count += 1

        if count == 5:
            break

    return recommended_movie_names, recommended_movie_posters


# -------------------------------
# Streamlit UI
# -------------------------------
st.set_page_config(page_title="Movie Recommender", layout="wide")

st.title("🎬 Movie Recommender System")

movie_list = movies['title'].values

selected_movie = st.selectbox(
    "Type or select a movie",
    movie_list
)


# -------------------------------
# Button click
# -------------------------------
if st.button('Show Recommendation'):

    names, posters = recommend(selected_movie)

    if len(names) == 0:
        st.error("Movie not found or no good recommendations available.")
    else:
        cols = st.columns(5)

        for i in range(len(names)):
            with cols[i]:
                st.text(names[i])
                st.image(posters[i])