import requests
import collections


# www.omdbapi.com


MovieResult = collections.namedtuple('MovieResult',
        'Title, Poster, Type, imdbID, Year')



search = 'capital'
url = 'http://www.omdbapi.com/?s={}'.format(search)

r = requests.get(url)
data = r.json()

results = data['Search']

# print(len(result))
#print(result[0])


#movie_1 = result[0]
#print(movie_1['Year'])

# improvement 1
# movies = []
# for result in results:
#   m = MovieResult(**result)
#   movies.append(m)

# improvement 2
# movies = [
#   MoviesResult(**m)
#   for m in results    
#
#]
# print (movies)




movies = []
for result in results:
    m = MovieResult(
            Title=result['Title'],
            Poster=result['Poster'],
            Type=result['Type'],
            imdbID=result['imdbID'],
            Year=result['Year']
    )
    movies.append(m)

print(movies[0])

