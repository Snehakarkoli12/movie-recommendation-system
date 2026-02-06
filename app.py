import streamlit as st
import pickle
import pandas as pd

# 1. Load the data
movies_dict = pickle.load(open('movie_dict.pkl', 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open('similarity.pkl', 'rb'))

# 2. Recommendation Logic
def recommend(movie):
    # Find the index of the movie in our dataframe
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    
    # Sort and pick the top 5 (excluding the movie itself at index 0)
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]
    
    recommended_movies = []
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies

# 3. Streamlit UI Design
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Which movie would you like to search for?',
    movies['title'].values
)

if st.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    st.write("### Top 5 Recommendations for you:")
    for i, movie in enumerate(recommendations):
        st.subheader(f"{i+1}. {movie}")