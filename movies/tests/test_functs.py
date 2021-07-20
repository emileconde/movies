import unittest
import sys, os
import requests
import tmdbsimple as tmdb

sys.path.append('../')
from popo.Movie import Movie, tv_show
from restutils.restutil import get_popular_movies, get_now_playing_movies, get_upcoming_movies, get_popular_tv
from restutils.parser import parse_movie_list, parse_tv_list, format_images


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