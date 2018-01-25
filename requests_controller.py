import requests

api_key = "edacb7eeacf9c2be67d32057dc199a0f"
resp = requests.get('https://api.themoviedb.org/3/movie/popular?api_key=edacb7eeacf9c2be67d32057dc199a0f&language=en-US&page=1')

if resp.status_code != 200:
    # This means something went wrong.
    print(resp.status_code)

# print(resp.json())

list_of_trailers = requests.get("https://api.themoviedb.org/3/movie/346364/videos?api_key="+api_key+"&language=en-US")

print(list_of_trailers.json()["results"][0]["key"])

# for movie in list_of_trailers.json()["results"]:
#     print(movie)