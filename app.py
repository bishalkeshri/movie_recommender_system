
import streamlit as st
import pickle
import pandas as pd
import requests
from streamlit_option_menu import option_menu
st.title("Movie Recommender System")

selected=option_menu(
        menu_title="Main Menu",
        options=["Home",'Action','Romantic','Fantasy','Animation','Comedy','Sci_Fi','Thriler','Mystery','Drama','Adventure','Horror','Family','Crime'],
    orientation="horizontal"

    )

if selected=="Action":

        st.title(f'{selected}')
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        action = pickle.load(open('action.pkl', 'rb'))
        Action = pd.DataFrame(action)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=a063f5c7aa3b749a58ef2cbf0abb2d58&language=en-US'.format(
                    movie_id))
            data = response.json()

            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            recommended_movies_posters = []

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        selected_movie_name = st.selectbox(
            "Select Movie",
            Action['title'].values
        )
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])

            with col2:
                st.text(names[1])
                st.image(posters[1])

            with col3:
                st.text(names[2])
                st.image(posters[2])

            with col4:
                st.text(names[3])
                st.image(posters[3])

            with col5:
                st.text(names[4])
                st.image(posters[4])



if selected=="Home":
        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=a063f5c7aa3b749a58ef2cbf0abb2d58&language=en-US'.format(
                    movie_id))
            data = response.json()

            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']

        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            recommended_movies_posters = []

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters

        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        similarity = pickle.load(open('similarity.pkl', 'rb'))


        selected_movie_name = st.selectbox(
            "Select Movie",
            movies['title'].values
        )
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])

            with col2:
                st.text(names[1])
                st.image(posters[1])

            with col3:
                st.text(names[2])
                st.image(posters[2])

            with col4:
                st.text(names[3])
                st.image(posters[3])

            with col5:
                st.text(names[4])
                st.image(posters[4])



if selected=="Adventure":

        st.title(f'{selected}')
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        action = pickle.load(open('adventure.pkl', 'rb'))
        Action = pd.DataFrame(action)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=a063f5c7aa3b749a58ef2cbf0abb2d58&language=en-US'.format(
                    movie_id))
            data = response.json()

            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            recommended_movies_posters = []

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        selected_movie_name = st.selectbox(
            "Select Movie",
            Action['title'].values
        )
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])

            with col2:
                st.text(names[1])
                st.image(posters[1])

            with col3:
                st.text(names[2])
                st.image(posters[2])

            with col4:
                st.text(names[3])
                st.image(posters[3])

            with col5:
                st.text(names[4])
                st.image(posters[4])







if selected=="Drama":

        st.title(f'{selected}')
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        action = pickle.load(open('drama.pkl', 'rb'))
        Action = pd.DataFrame(action)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=a063f5c7aa3b749a58ef2cbf0abb2d58&language=en-US'.format(
                    movie_id))
            data = response.json()

            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            recommended_movies_posters = []

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        selected_movie_name = st.selectbox(
            "Select Movie",
            Action['title'].values
        )
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])

            with col2:
                st.text(names[1])
                st.image(posters[1])

            with col3:
                st.text(names[2])
                st.image(posters[2])

            with col4:
                st.text(names[3])
                st.image(posters[3])

            with col5:
                st.text(names[4])
                st.image(posters[4])









if selected=="Mystery":

        st.title(f'{selected}')
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        action = pickle.load(open('mystery.pkl', 'rb'))
        Action = pd.DataFrame(action)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=a063f5c7aa3b749a58ef2cbf0abb2d58&language=en-US'.format(
                    movie_id))
            data = response.json()

            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            recommended_movies_posters = []

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        selected_movie_name = st.selectbox(
            "Select Movie",
            Action['title'].values
        )
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])

            with col2:
                st.text(names[1])
                st.image(posters[1])

            with col3:
                st.text(names[2])
                st.image(posters[2])

            with col4:
                st.text(names[3])
                st.image(posters[3])

            with col5:
                st.text(names[4])
                st.image(posters[4])








if selected=="Thriler":

        st.title(f'{selected}')
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        action = pickle.load(open('thriler.pkl', 'rb'))
        Action = pd.DataFrame(action)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=a063f5c7aa3b749a58ef2cbf0abb2d58&language=en-US'.format(
                    movie_id))
            data = response.json()

            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            recommended_movies_posters = []

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        selected_movie_name = st.selectbox(
            "Select Movie",
            Action['title'].values
        )
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])

            with col2:
                st.text(names[1])
                st.image(posters[1])

            with col3:
                st.text(names[2])
                st.image(posters[2])

            with col4:
                st.text(names[3])
                st.image(posters[3])

            with col5:
                st.text(names[4])
                st.image(posters[4])








if selected=="Sci_Fi":

        st.title(f'{selected}')
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        action = pickle.load(open('sci_fi.pkl', 'rb'))
        Action = pd.DataFrame(action)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=a063f5c7aa3b749a58ef2cbf0abb2d58&language=en-US'.format(
                    movie_id))
            data = response.json()

            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            recommended_movies_posters = []

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        selected_movie_name = st.selectbox(
            "Select Movie",
            Action['title'].values
        )
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])

            with col2:
                st.text(names[1])
                st.image(posters[1])

            with col3:
                st.text(names[2])
                st.image(posters[2])

            with col4:
                st.text(names[3])
                st.image(posters[3])

            with col5:
                st.text(names[4])
                st.image(posters[4])






if selected=="Comedy":

        st.title(f'{selected}')
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        action = pickle.load(open('comedy.pkl', 'rb'))
        Action = pd.DataFrame(action)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=a063f5c7aa3b749a58ef2cbf0abb2d58&language=en-US'.format(
                    movie_id))
            data = response.json()

            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            recommended_movies_posters = []

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        selected_movie_name = st.selectbox(
            "Select Movie",
            Action['title'].values
        )
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])

            with col2:
                st.text(names[1])
                st.image(posters[1])

            with col3:
                st.text(names[2])
                st.image(posters[2])

            with col4:
                st.text(names[3])
                st.image(posters[3])

            with col5:
                st.text(names[4])
                st.image(posters[4])







if selected=="Animation":

        st.title(f'{selected}')
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        action = pickle.load(open('animation.pkl', 'rb'))
        Action = pd.DataFrame(action)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=a063f5c7aa3b749a58ef2cbf0abb2d58&language=en-US'.format(
                    movie_id))
            data = response.json()

            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            recommended_movies_posters = []

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        selected_movie_name = st.selectbox(
            "Select Movie",
            Action['title'].values
        )
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])

            with col2:
                st.text(names[1])
                st.image(posters[1])

            with col3:
                st.text(names[2])
                st.image(posters[2])

            with col4:
                st.text(names[3])
                st.image(posters[3])

            with col5:
                st.text(names[4])
                st.image(posters[4])








if selected=="Fantasy":

        st.title(f'{selected}')
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        action = pickle.load(open('fantasy.pkl', 'rb'))
        Action = pd.DataFrame(action)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=a063f5c7aa3b749a58ef2cbf0abb2d58&language=en-US'.format(
                    movie_id))
            data = response.json()

            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            recommended_movies_posters = []

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        selected_movie_name = st.selectbox(
            "Select Movie",
            Action['title'].values
        )
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])

            with col2:
                st.text(names[1])
                st.image(posters[1])

            with col3:
                st.text(names[2])
                st.image(posters[2])

            with col4:
                st.text(names[3])
                st.image(posters[3])

            with col5:
                st.text(names[4])
                st.image(posters[4])







if selected=="Crime":

        st.title(f'{selected}')
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        action = pickle.load(open('crime.pkl', 'rb'))
        Action = pd.DataFrame(action)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=a063f5c7aa3b749a58ef2cbf0abb2d58&language=en-US'.format(
                    movie_id))
            data = response.json()

            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            recommended_movies_posters = []

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        selected_movie_name = st.selectbox(
            "Select Movie",
            Action['title'].values
        )
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])

            with col2:
                st.text(names[1])
                st.image(posters[1])

            with col3:
                st.text(names[2])
                st.image(posters[2])

            with col4:
                st.text(names[3])
                st.image(posters[3])

            with col5:
                st.text(names[4])
                st.image(posters[4])







if selected=="Horror":

        st.title(f'{selected}')
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        action = pickle.load(open('horror.pkl', 'rb'))
        Action = pd.DataFrame(action)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=a063f5c7aa3b749a58ef2cbf0abb2d58&language=en-US'.format(
                    movie_id))
            data = response.json()

            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            recommended_movies_posters = []

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        selected_movie_name = st.selectbox(
            "Select Movie",
            Action['title'].values
        )
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])

            with col2:
                st.text(names[1])
                st.image(posters[1])

            with col3:
                st.text(names[2])
                st.image(posters[2])

            with col4:
                st.text(names[3])
                st.image(posters[3])

            with col5:
                st.text(names[4])
                st.image(posters[4])








if selected=="Romantic":

        st.title(f'{selected}')
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        action = pickle.load(open('romantic.pkl', 'rb'))
        Action = pd.DataFrame(action)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=a063f5c7aa3b749a58ef2cbf0abb2d58&language=en-US'.format(
                    movie_id))
            data = response.json()

            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            recommended_movies_posters = []

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        selected_movie_name = st.selectbox(
            "Select Movie",
            Action['title'].values
        )
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])

            with col2:
                st.text(names[1])
                st.image(posters[1])

            with col3:
                st.text(names[2])
                st.image(posters[2])

            with col4:
                st.text(names[3])
                st.image(posters[3])

            with col5:
                st.text(names[4])
                st.image(posters[4])






if selected=="Family":

        st.title(f'{selected}')
        movies_dict = pickle.load(open('movies_dict.pkl', 'rb'))
        movies = pd.DataFrame(movies_dict)

        action = pickle.load(open('family.pkl', 'rb'))
        Action = pd.DataFrame(action)
        similarity = pickle.load(open('similarity.pkl', 'rb'))

        def fetch_poster(movie_id):
            response = requests.get(
                'https://api.themoviedb.org/3/movie/{}?api_key=a063f5c7aa3b749a58ef2cbf0abb2d58&language=en-US'.format(
                    movie_id))
            data = response.json()

            return "https://image.tmdb.org/t/p/w500/" + data['poster_path']


        def recommend(movie):
            movie_index = movies[movies['title'] == movie].index[0]
            distances = similarity[movie_index]
            movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

            recommended_movies = []
            recommended_movies_posters = []

            for i in movies_list:
                movie_id = movies.iloc[i[0]].movie_id

                recommended_movies.append(movies.iloc[i[0]].title)
                recommended_movies_posters.append(fetch_poster(movie_id))
            return recommended_movies, recommended_movies_posters


        selected_movie_name = st.selectbox(
            "Select Movie",
            Action['title'].values
        )
        if st.button('Recommend'):
            names, posters = recommend(selected_movie_name)
            col1, col2, col3, col4, col5 = st.columns(5)
            with col1:
                st.text(names[0])
                st.image(posters[0])

            with col2:
                st.text(names[1])
                st.image(posters[1])

            with col3:
                st.text(names[2])
                st.image(posters[2])

            with col4:
                st.text(names[3])
                st.image(posters[3])

            with col5:
                st.text(names[4])
                st.image(posters[4])








