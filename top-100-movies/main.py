import requests
from bs4 import BeautifulSoup
import json

class_ = "jsx-952983560"
response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
response.raise_for_status()

content = response.text

soup = BeautifulSoup(content, "html.parser")

script = soup.find_all(name="script", id="__NEXT_DATA__")[0]
script = str(script)[len('<script id="__NEXT_DATA__" type="application/json">'):-9]

script = json.loads(script)

script = script['props']["pageProps"]["apolloState"]

list_of_movies = []
counter = 100
for (key, value) in script.items():
    if key.startswith("Image"):
        movie_title = script[key]["titleText"]
        if movie_title.find(")") == -1:
            movie_title = f"{counter}) {movie_title}"
        counter -= 1
        list_of_movies.append(movie_title)

list_of_movies.reverse()
for movie in list_of_movies:
    print(movie)
with open("list.txt", 'w') as file:
    for movie in list_of_movies:
        file.write(movie+ "\n")

# movie_titles = soup.find_all(name="img", class_="jsx-952983560 loading")
#
# movie_list = []
# counter = 1
# for title in movie_titles:
#     alt = title.get("alt")
#     if alt:
#         movie = alt
#         if movie not in movie_list:
#             movie_list.append(movie)
#             counter += 1
#
# for movie in movie_list:
#     print(movie)