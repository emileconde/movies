import unittest
import sys, os
import requests
import tmdbsimple as tmdb

sys.path.append('../')
from popo.Movie import Movie, tv_show
from restutils.restutil import *
from restutils.parser import *


class TestFuctions(unittest.TestCase):
    
    
    def test_pop_movies(self):
        #moviesObject = tmdb.Movies()
        #popular_movies = moviesObject.popular(maximum=1)
        self.assertNotEqual(get_popular_movies(), None)
    
    
    def test_now_play_movies(self):
        #moviesObject = tmdb.Movies()
        #now_playing = moviesObject.now_playing()
        self.assertNotEqual(get_now_playing_movies(), None)
    
    
    def test_upcom_movies(self):
        #moviesObject = tmdb.Movies()
        #upcoming_movies = moviesObject.upcoming()
        self.assertNotEqual(get_upcoming_movies(), None)
    
    
    def test_pop_tv(self):
        #tvObject = tmdb.TV()
        #popular_tv = tvObject.popular()
        self.assertNotEqual(get_popular_tv(), None)
    
    
    def test_recommendations(self):
        movie_id = "385128" #Movie == F9
        self.assertNotEqual(get_recommendations(movie_id),None)
    
    
    def test_reviews(self):
        movie_id = "385128" #Movie == F9
        self.assertNotEqual(get_reviews(movie_id),None)
    
    
    def test_trailers(self):
        movie_id = "385128"
        self.assertNotEqual(get_trailers(movie_id), None)
    
    
    def test_mov_by_id(self):
        movie_id = "385128"
        self.assertNotEqual(get_movie_by_id(movie_id), None)
    
    
    def test_search(self):
        self.assertEqual(search(""), "")
        query = "bourne"
        self.assertNotEqual(search(query), None)
    
    
    def test_find(self):
        #call single movie function to return movie object
        #return movie.id
        movie_id = "385128"
        mov_object = get_movie_by_id(movie_id)
        self.assertNotEqual(find(mov_object.id), None)
    
    
    def test_movie_parse(self):
        self.assertEqual(parse_movie_list(None),"")
        moviesObject = tmdb.Movies()
        popular_movies = moviesObject.popular(maximum=1)
        self.assertNotEqual(parse_movie_list(popular_movies), None)
    
    
    def test_tv_parse(self):
        self.assertEqual(parse_tv_list(None), "")
        tvObject = tmdb.TV()
        popular_tv = tvObject.popular()
        self.assertNotEqual(parse_tv_list(popular_tv), None)
    
    
if __name__ == '__main__':
    unittest.main()