import tmdbsimple as tmdb
tmdb.API_KEY = '3c41c56169da154b8c4b090993284bf8'
import requests
tmdb.REQUESTS_SESSION = requests.Session()


auth = tmdb.Authentication()
response = auth.token_validate_with_login(username = 'seoproject2', password='movies', request_token='e6fcae98134cb958f1a5dadf6f7bb208104f6b43')
token = response['request_token']
session_id = auth.session_new(token_id = token)
print(session_id)
