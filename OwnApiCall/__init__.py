import os
import requests

TMDB_API_KEY=os.environ.get('TMDB_API_KEY', None)

session = requests.Session()
session.params={}
session.params['api_key']=TMDB_API_KEY

from .OwnApiCall import Movie