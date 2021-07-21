import unittest
import sys

sys.path.append('../')
from main import app

class BasicTests(unittest.TestCase):

    # executed prior to each test
    def setUp(self):
        self.app = app.test_client()

    ###############
    #### tests ####
    ###############

    def test_home_page(self):
        response = self.app.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)

    def test_movie_details(self):
        response = self.app.get("/details/520763", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        
    def test_list(self):
        response = self.app.get("/list", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
    
if __name__ == '__main__':
    unittest.main()
