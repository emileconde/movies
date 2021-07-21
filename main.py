from flask import Flask, render_template, url_for, flash, redirect
from restutils.restutil import get_popular_movies, get_upcoming_movies, get_now_playing_movies, get_popular_tv, get_top_rated_movies
import requests
import json
# from turbo_flask import Turbo

app = Flask(__name__)

upcoming_movies = get_upcoming_movies()
now_playing = get_now_playing_movies()
popular_movies = get_popular_movies()
top_rated_movies = get_top_rated_movies()
tv_series = get_popular_tv()


@app.route("/")
def home():
    return render_template(
        'home.html',
        upcoming_movies=upcoming_movies,
        now_playing=now_playing,
        popular_movies=popular_movies,
        tv_series=tv_series,
        top_rated_movies=top_rated_movies)

# @app.route("/")
# def home():
#     return render_template("movie_detail.html")

@app.route("/details/<movie_id>")
def movie_detail(movie_id):
    converted_id = int(movie_id)
    for movie in popular_movies:
        if movie.id == converted_id:
            return render_template("movie_detail.html", movie=movie)
    return render_template("movie_detail.html")


@app.route("/list")
def movie_list():
    return render_template("list.html")

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
