import pickle
import difflib

import pandas as pd
import streamlit as st
import pandas as pd

movies_data = pickle.load(open("movies_data.pkl", 'rb'))
# movies_data = pd.read_csv(r"E:\Movie_recommendation_system\movies_data.pkl")
similarity = pickle.load(open("similarity.pkl", 'rb'))


st.title("MOVIE RECOMMENDATION SYSTEM")
st.write('###### Movie Name :- ')
movie_name = st.text_input('')

try:
    list_of_all_titles = movies_data['title'].tolist()

    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)

    close_match = find_close_match[0]

    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]

    similarity_score = list(enumerate(similarity[index_of_the_movie]))

    sorted_similar_movies = sorted(similarity_score, key=lambda x: x[1], reverse=True)

    st.write('###### Movies Suggested For You : ')

    i = 1


    for movie in sorted_similar_movies:
        index = movie[0]
        title_from_index = movies_data[movies_data.index == index]['title'].values[0]
        if (i<11):
            st.write(i, " - ", title_from_index)
            i += 1


except IndexError:
    st.write('###### No Similar Movies')

except:
    st.write('No Similar Movies')

