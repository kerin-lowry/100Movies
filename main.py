from bs4 import BeautifulSoup
import requests

URL="https://www.timeout.com/newyork/movies/best-movies-of-all-time"

response = requests.get(URL)

soup = BeautifulSoup(response.text, "html.parser")
movies = soup.find_all(name="h3", class_="card-title")

movie_list = []

for movie in movies:
    movie_list.append(movie.getText().replace("\n\n                    ","").replace("\n                    \n", "").replace("\xa0", ""))
movie_list = movie_list[:-1]

with open("movies.txt", "w") as file:
    for movie in movie_list:
        file.write(f"{movie}\n")