from flask import Flask, render_template, url_for, flash, redirect, request, session, flash
from restutils.restutil import get_popular_movies, get_upcoming_movies, get_now_playing_movies, get_popular_tv, get_top_rated_movies, get_recommendations, get_reviews, get_movie_by_id, search, get_trailers, get_tv_reviews, get_tv_recommendation
import requests


app = Flask(__name__)
app.secret_key = "4534545gvg787478w"

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
    trailer = get_trailers(movie_id)
    return render_template("movie_detail.html", movie=movie, recommended_list=recommended_list, reviews=reviews, trailer=trailer)


@app.route("/search")
def search_form():
    return render_template("search.html")

@app.route("/series")
def serie_list():
    return render_template("serie_list.html", series=tv_series)


@app.route("/seacrh_by_title", methods=["POST"])
def seacrh_by_title():
    title = request.form["title"]
    year = request.form["year"]
    if year != "":
        data = search(title, year)
    else:
        data = search(title, "")
    movies = data
    return render_template("search.html",movies=movies) 




@app.route("/favorite_list")
def favorite_list():
    favorite_list = session.get("favorite")
    if favorite_list == None:
        flash("The favorite list is empty")
        return redirect(url_for("home"))
    else:
        return render_template("favorite.html", favorite_list=favorite_list) 





@app.route("/add_to_favorite/<movie_id>")
def add_to_favorite(movie_id):
    favorite_list = {}
    if "favorite" in session:
        favorite_list = session.get("favorite")
    else:
        session["favorite"] = {}

    favorite_list[movie_id] = movie_id
    
    session["favorite"] = favorite_list
    return redirect(url_for("home"))        
        
        


@app.route("/remove_from_list/<movie_id>")
def remove_from_list(movie_id):
    favorite_list = session.get("favorite")
    favorite_list.pop(movie_id,None)
    session["favorite"] = favorite_list
    return redirect(url_for("favorite_list"))




@app.route("/serie_detail/<serie_id>")
def serie_detail(serie_id):
    converted_id = int(serie_id)
    for serie in tv_series:       
        if serie.id == converted_id:
            recommended_list = get_tv_recommendation(serie.id)
            reviews = get_tv_reviews(serie.id)
            return render_template("serie_detail.html", serie=serie, recommended_list=recommended_list, reviews=reviews)
    return "Nothing was found"

    

@app.route("/list")
def now_playing_list():
    return render_template("now_playing.html", movies=now_playing)
  
    

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
