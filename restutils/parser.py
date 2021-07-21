from popo.Movie import Movie, tv_show, review

POSTER_SIZE = "w500"
BACKDROP_SIZE = "original"
BASE_IMG_URL = "https://image.tmdb.org/t/p/"
BASE_TRAILER_URL = "https://www.youtube.com/watch?v="


def parse_movie_list(results):

    if(results is None):
        print("Nothing was returned")
        return ""

    list_of_movies = []
    movielist = results['results']
    for i in range(len(movielist)):
        id = movielist[i].get("id")
        title = movielist[i].get("title")
        overview = movielist[i].get("overview")
        popularity = movielist[i].get("popularity")
        backdrop_path = format_images(
            BACKDROP_SIZE, movielist[i].get("backdrop_path"))
        poster_path = format_images(
            POSTER_SIZE, movielist[i].get("poster_path"))
        release_date = movielist[i].get("release_date")
        vote_average = movielist[i].get("vote_average")
        movieObject = Movie(
            id,
            title,
            overview,
            popularity,
            backdrop_path,
            poster_path,
            release_date,
            vote_average)
        list_of_movies.append(movieObject)
    return list_of_movies


def parse_tv_list(results):

    if(results is None):
        print("Nothing was returned")
        return ""

    list_of_tv_shows = []
    tvlist = results['results']
    for i in range(len(tvlist)):
        id = tvlist[i].get("id")
        name = tvlist[i].get("name")
        overview = tvlist[i].get("overview")
        backdrop_path = format_images(
            BACKDROP_SIZE, tvlist[i].get("backdrop_path"))
        poster_path = format_images(POSTER_SIZE, tvlist[i].get("poster_path"))
        first_air_date = tvlist[i].get("first_air_date")
        vote_average = tvlist[i].get("vote_average")
        tvObject = tv_show(id, name, overview, poster_path,
                           backdrop_path, vote_average, first_air_date)
        list_of_tv_shows.append(tvObject)
    return list_of_tv_shows



def parse_reviews(results):
     
    if(results is None):
        print("Nothing was returned")
        return ""
    
    parsed_reviews = []
    review_list = results['results']
    for i in range(len(review_list)):
        author = review_list[i].get('author')
        content = review_list[i].get('content')
        reviewObject = review(author, content)
        parsed_reviews.append(reviewObject)
    return parsed_reviews


def parse_trailer(key):
    return BASE_TRAILER_URL+key


"""Contructs a uri from the paths"""
def format_images(size, path):
    if path is not None:
        if size == POSTER_SIZE:
            size = POSTER_SIZE
        else:
            size = BACKDROP_SIZE
    else:
        return ""
    return BASE_IMG_URL + size + path


# print(type(POSTER_SIZE))
