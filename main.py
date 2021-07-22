from flask import Flask, render_template, url_for, flash, redirect
from restutils.restutil import get_popular_movies, get_upcoming_movies, get_now_playing_movies, get_popular_tv, get_top_rated_movies, get_recommendations, get_reviews, get_movie_by_id, search
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
         popular_movies=popular_movies)


@app.route("/details/<movie_id>")
def movie_detail(movie_id):
    movie = get_movie_by_id(movie_id)
    recommended_list = get_recommendations(movie_id)
    reviews = get_reviews(movie_id)
    return render_template("movie_detail.html", movie=movie, recommended_list=recommended_list, reviews=reviews)


@app.route("/seacrh_by_title", methods=["POST"])
def seacrh_by_title():
    title = request.form["title"]
    year = request.form["year"]
    if year != "":
        rawData = requests.get("http://www.omdbapi.com/?apikey=15df6171&t="+title+"&y="+year)
    else:
        rawData = requests.get("http://www.omdbapi.com/?apikey=15df6171&t="+title)
    movie = rawData.json()
    return render_template("search.html",movie=movie) 


# @app.route("/series/<serie_id>")
# def serie_detail(serie_id):
#     converted_id = int(serie_id)
#     for movie_list in all_movies:
#             for serie in movie_list:
#                 if serie.id == converted_id:
#                     return render_template("serie_detail.html", serie=serie)
#     return render_template("serie_detail.html")


# @app.route("/list")
# def popular_movie_list():
#     return render_template("list.html", movies=popular_movies)
  
    
# @app.route("/list")
# def top_rated_list():
#     return render_template("list.html", movies=top_rated_movies)
        
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
