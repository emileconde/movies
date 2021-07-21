"""autopep8 --in-place --aggressive --aggressive <filename>"""
"""This class contains all the utility/helper methods associated with communicating with the API_KEY
It uses helper methods from the parser.py to parse the json file and return objects."""

import requests
import tmdbsimple as tmdb
from restutils.parser import parse_movie_list, parse_tv_list, parse_reviews, parse_trailer
tmdb.API_KEY = '3c41c56169da154b8c4b090993284bf8'
tmdb.REQUESTS_SESSION = requests.Session()

"""id, title, overview, popularity, backdrop_path, poster_path, reslease_date"""


def get_popular_movies():
    moviesObject = tmdb.Movies()
    popular_movies = moviesObject.popular(maximum=1)
    return parse_movie_list(popular_movies)


def get_now_playing_movies():
    moviesObject = tmdb.Movies()
    now_playing = moviesObject.now_playing()
    return parse_movie_list(now_playing)


def get_upcoming_movies():
    moviesObject = tmdb.Movies()
    upcoming_movies = moviesObject.upcoming()
    return parse_movie_list(upcoming_movies)


def get_top_rated_movies():
    moviesObject = tmdb.Movies()
    top_rated_movies = moviesObject.top_rated()
    return parse_movie_list(top_rated_movies)


def get_popular_tv():
    tvObject = tmdb.TV()
    popular_tv = tvObject.popular()
    return parse_tv_list(popular_tv)


def get_recommendations(movie_id):
    moviesObject = tmdb.Movies(movie_id)
    recommendations = moviesObject.recommendations()
    return parse_movie_list(recommendations)


def get_reviews(movie_id):
    moviesObject = tmdb.Movies(movie_id)
    reviews = moviesObject.reviews()
    return parse_reviews(reviews)


def get_trailers(movie_id):
    moviesObject = tmdb.Movies(movie_id)
    videos = moviesObject.videos()
    single_trailer_key = videos['results'][0].get('key')
    return parse_trailer(single_trailer_key)


def find(id):
    ob_ject = tmdb.Find(id=id)
    value = ob_ject.info()
    return value

