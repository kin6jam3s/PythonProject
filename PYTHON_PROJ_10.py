from movie_client import MovieClient
import requests.exceptions

def main():
    print_header()
    search_event_loop()


def print_header():
    print('------------------------')
    print(' MOVIE SEARCH APP')
    print('------------------------')
    print()


def search_event_loop():
    search = None # 'ONCE_THROUGH_LOOP'

    while search != 'x':
        try:
            search = input('Title search text (x to exit): ')
            if search != 'x':
                client = MovieClient(search)

                results = client.perform_search()
                print("Found {} results.".format(len(results)))
                for r in results:
                    print("{} -- {}".format(r.Year, r.Title))
        except requests.exceptions.ConnectionError as ce:
            print('ERROR: Connot search, your network is down.')
        except ValueError as ve:
            print('Your search string is invalid: {}'.format(ve))
        except Exception as x:
            print('ERROR {}'.format(x))

    print('exiting...')

if __name__ == '__main__':
    main()








# import requests
# import collections
#
#
# # www.omdbapi.com
#
#
# MovieResult = collections.namedtuple('MovieResult',
#         'Title, Poster, Type, imdbID, Year')
#
#
#
# search = 'capital'
# url = 'http://www.omdbapi.com/?s={}'.format(search)
#
# r = requests.get(url)
# data = r.json()
#
# results = data['Search']
#
# # print(len(result))
# #print(result[0])
#
#
# #movie_1 = result[0]
# #print(movie_1['Year'])
#
# # improvement 1
# # movies = []
# # for result in results:
# #   m = MovieResult(**result)
# #   movies.append(m)
#
# # improvement 2
# # movies = [
# #   MoviesResult(**m)
# #   for m in results
# #
# #]
# # print (movies)
#
#
#
#
# movies = []
# for result in results:
#     m = MovieResult(
#             Title=result['Title'],
#             Poster=result['Poster'],
#             Type=result['Type'],
#             imdbID=result['imdbID'],
#             Year=result['Year']
#     )
#     movies.append(m)
#
# print(movies[0])
#
