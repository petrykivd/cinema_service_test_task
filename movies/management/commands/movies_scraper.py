import string

import requests
from django.core.management import BaseCommand

from movies.models import Movie, Genre, Actor


API_KEY = "2843bc95"


def populate_database(api_key):

    alphabet = string.ascii_lowercase

    start_url = f"https://www.omdbapi.com/?apikey={api_key}&t=a"
    for letter in alphabet:
        url = start_url + letter
        response = requests.get(f"{url}")
        data = response.json()
        title = data["Title"]
        release_year = data["Year"][0:4]
        runtime = data["Runtime"].split(" ")[0]
        genres = data["Genre"].split(", ")
        director = data["Director"]
        actors = data["Actors"].split(", ")
        description = data["Plot"]
        country = data["Country"]
        poster_url = data["Poster"]
        imdb = data["imdbRating"]

        movie = Movie(
            title=title,
            release_year=release_year,
            runtime=int(runtime),
            director=director,
            description=description,
            country=country,
            poster_url=poster_url,
            imdb=float(imdb)
        )

        # Збереження об'єкта в базі даних
        movie.save()

        # Додавання жанрів та акторів до об'єкта Movie
        for genre_name in genres:
            # Перевірка наявності жанру в базі даних
            genre, _ = Genre.objects.get_or_create(name=genre_name)
            movie.genres.add(genre)

        for actor_name in actors:
            # Перевірка наявності актора в базі даних
            actor, _ = Actor.objects.get_or_create(full_name=actor_name)
            movie.actors.add(actor)
        url = start_url


class Command(BaseCommand):
    """Django command to pause execution until db is available"""

    def handle(self, *args, **options):
        populate_database(api_key=API_KEY)
