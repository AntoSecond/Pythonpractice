import os
import requests
import json
import webbrowser

#from . import session


TMDB_API_KEY=os.environ.get('TMDB_API_KEY', None)

#session = requests.Session()
#session.params={}
#session.params['api_key']=TMDB_API_KEY
#print(session.params['api_key'])
#print(type(session))

class Movie(object):
    def __init__(self, id):
        self.id=id
        print("initiated ID {}".format(self.id))


    def GetExtID(self):
        self.id=464835
        path='https://api.themoviedb.org/3/movie/{}/external_ids?api_key={}'.format(self.id, TMDB_API_KEY)
        string=requests.get(path)
        string=string.json()
        return string['imdb_id']
        #return string['imdb_id']




    def function2(self):
        pass




imdb=Movie.GetExtID(Movie(564835))

path='https://www.imdb.com/title/{}'.format(imdb)
print(imdb)
print(path)
webbrowser.open('https://www.imdb.com/title/{}'.format(imdb))

#TMDB_API_KEY=os.environ(TMDB_API_KEY, None)

#session=requests.Session()
#session.params={}
#session=requests.get('https://api.themoviedb.org/3/trending/all/day?api_key=5eb51ab1040e271fa7b1b5d9ac5cc3ab')
#with open('text.txt', 'w') as file:
#    for line in session.text:
#        file.writelines(line)

#print(session.date)
#https://api.themoviedb.org/3/find/{external_id}?api_key=5eb51ab1040e271fa7b1b5d9ac5cc3ab&language=en-US&external_source=imdb_id


#trending=requests.get('https://api.themoviedb.org/3/trending/all/day?api_key=5eb51ab1040e271fa7b1b5d9ac5cc3ab')
#trending1 =trending.json()
#results=(trending1['results'])
#print(results[2])
#print(dir(trending))
#print(dir(trending1))
#print(dir(results))
#print(dir(results[2]))

#print(results[2]['adult'])


#json.loads take a string as input and returns a dictionary as output.
#json.dumps take a dictionary as input and returns a string as output.




#https://api.themoviedb.org/3/movie/1234/external_ids?api_key=5eb51ab1040e271fa7b1b5d9ac5cc3ab

#https://api.themoviedb.org/3/genre/movie/list?api_key=5eb51ab1040e271fa7b1b5d9ac5cc3ab&language=en-US
#https://api.themoviedb.org/3/trending/all/day?api_key=5eb51ab1040e271fa7b1b5d9ac5cc3ab
#https://developers.themoviedb.org/3/movies/get-popular-movies