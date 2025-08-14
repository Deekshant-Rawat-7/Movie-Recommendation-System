import pickle
import streamlit as st
import requests
import base64
from PIL import Image



st.set_page_config(page_title='Movie Recommendation', page_icon= "🎬") 

def add_bg(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg('./images/image.jpg')    





def fetch_poster(movie_id):
    url = "https://api.themoviedb.org/3/movie/{}?api_key=3842ffb1938d63baff14309628e7da91&language=en-US".format(movie_id)
    data = requests.get(url)
    data = data.json()
    poster_path = data['poster_path']
    full_path = "https://image.tmdb.org/t/p/w500/" + poster_path
    return full_path

def recommend(movie):
    index = movies[movies['title'] == movie].index[0]
    distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
    recommended_movie_names = []
    recommended_movie_posters = []
    for i in distances[1:7]:
        # fetch the movie poster
        movie_id = movies.iloc[i[0]].movie_id
        recommended_movie_posters.append(fetch_poster(movie_id))
        recommended_movie_names.append(movies.iloc[i[0]].title)

    return recommended_movie_names,recommended_movie_posters








st.markdown(""" <style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style> """, unsafe_allow_html=True)

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)
    
    
  

    
    

st.header('THE MOVIE RECOMMENDATION SYSTEM')


image = Image.open('./images/image2.jpg')

st.image(image, caption=None, width=None, use_column_width=True, clamp=False, channels="RGB", output_format="JPG")
#st.image(image, caption='Movie Roll')    
    


movies = pickle.load(open('C:/Users/ASUS/Desktop/major/movie-recommender-system/movie_list.pkl','rb'))
similarity = pickle.load(open('C:/Users/ASUS/Desktop/major/movie-recommender-system/similarity.pkl','rb'))

movie_list = movies['title'].values
selected_movie = st.selectbox("TYPE OR SELECT A MOVIE", movie_list)

if st.button('SHOW MY RECOMMENDATION'):
    recommended_movie_names,recommended_movie_posters = recommend(selected_movie)
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    with col1:
        st.text(recommended_movie_names[0])
        st.image(recommended_movie_posters[0])
    with col2:
        st.text(recommended_movie_names[1])
        st.image(recommended_movie_posters[1])

    with col3:
        st.text(recommended_movie_names[2])
        st.image(recommended_movie_posters[2])
    with col4:
        st.text(recommended_movie_names[3])
        st.image(recommended_movie_posters[3])
    with col5:
        st.text(recommended_movie_names[4])
        st.image(recommended_movie_posters[4])
    with col6:
        st.text(recommended_movie_names[5])
        st.image(recommended_movie_posters[5])





