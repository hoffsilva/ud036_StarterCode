import media
import fresh_tomatoes
import requests
import json

default_url = "https://api.themoviedb.org/3/movie/popular?"
api_key = "api_key="
# set the default idiom to get info about movies
lang_set = "&language=en-US"
number_page = "&page=1"
full_url = default_url + api_key + lang_set + number_page

youtube_url = "https://www.youtube.com/watch?v="

movies_url = "https://api.themoviedb.org/3/movie/"

list_of_movies = requests.get(full_url)

if list_of_movies.status_code != 200:
    # This means something went wrong.
    print(list_of_movies.status_code)

array_of_movies = []


# get poster url
def get_poster_url_by(poster_path):
    poster_url = "https://image.tmdb.org/t/p/w600_and_h900_bestv2"+poster_path
    return poster_url


# get trailer url
def get_trailer_url_by(movie_id):
    trailers_api_url = movies_url+str(movie_id)+"/videos?"+api_key+lang_set
    trailer_object = requests.get(trailers_api_url)
    print(trailer_object)
    trailer_url = youtube_url + str(trailer_object.json()["results"][0]["key"])
    return trailer_url


# create a movie object
def get_movie_data(movie):
    print(movie)
    title = movie['title'].encode('ascii', 'ignore')
    overview = movie['overview'].encode('ascii', 'ignore')
    poster_path = movie['poster_path']
    id = movie['id']
    vote_average = movie['vote_average']
    popularity = movie['popularity']
    release_date = movie["release_date"]
    data_movie = media.Movie(
        title,
        overview,
        get_poster_url_by(poster_path),
        get_trailer_url_by(id),
        vote_average,
        popularity,
        release_date
    )
    return data_movie


# populates the array with movie objects
json_list = json.loads(list_of_movies.text)["results"]

for movie_item in json_list:
    array_of_movies.append(get_movie_data(movie_item))


fresh_tomatoes.open_movies_page(array_of_movies)
