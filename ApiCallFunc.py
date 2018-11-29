import os
import requests
import json
global TMDB_API_KEY
#TMDB_API_KEY = os.environ(TMDB_API_KEY, None)
TMDB_API_KEY= '5eb51ab1040e271fa7b1b5d9ac5cc3ab'

print(TMDB_API_KEY)


def GetExtID(id):
    path = 'https://api.themoviedb.org/3/movie/{}/external_ids?api_key={}'.format(id, TMDB_API_KEY)
    string = requests.get(path)
    string = string.json()
    print(string)
    return string['imdb_id']

def GenerateID(query):
    path = 'https://api.themoviedb.org/3/search/movie?api_key={}&language=en-US&page=1&include_adult=false&query={}'.format(TMDB_API_KEY, query)
    string = requests.get(path)
    string = string.json()
    pages=string['total_pages']
    with open('text.txt', 'w') as openfile:
        for x in range(1,pages):
            path = 'https://api.themoviedb.org/3/search/movie?api_key={}&language=en-US&page={}&include_adult=false&query={}'.format(TMDB_API_KEY, x, query)
            string = requests.get(path)
            string = string.json()
            results = string['results']
            for dicts in results:
                openfile.writelines('{} - {}\n'.format(dicts['title'], dicts['popularity']))
    return results[0]
   # https: //api.themoviedb.org/3/keyword/action?api_key=5eb51ab1040e271fa7b1b5d9ac5cc3ab


#print(GetExtID(564835))
print(GenerateID('action'))

#GenerateID(action)