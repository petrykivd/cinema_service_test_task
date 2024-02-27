from django.test import TestCase
from django.urls import reverse
from movies.models import Actor, Genre, Movie


class MovieModelTestCase(TestCase):
    def setUp(self):
        self.actor = Actor.objects.create(full_name="John Doe")
        self.genre = Genre.objects.create(name="Action")
        self.movie = Movie.objects.create(
            title="Test Movie",
            release_year=2022,
            director="Test Director",
            runtime=120,
            imdb=7.5,
            country="USA",
            description="Test Description",
            poster_url="https://example.com"
        )

    def test_movie_creation(self):
        self.assertEqual(self.movie.title, "Test Movie")
        self.assertEqual(self.movie.release_year, 2022)
        self.assertEqual(self.movie.director, "Test Director")

    def test_movie_actor_relationship(self):
        self.movie.actors.add(self.actor)
        self.assertIn(self.actor, self.movie.actors.all())

    def test_movie_genre_relationship(self):
        self.movie.genres.add(self.genre)
        self.assertIn(self.genre, self.movie.genres.all())


class ViewsTestCase(TestCase):
    def test_index_view(self):
        response = self.client.get(reverse("movies:index"))
        self.assertEqual(response.status_code, 200)

    def test_movie_list_view(self):
        response = self.client.get(reverse("movies:movie-list"))
        self.assertEqual(response.status_code, 200)

    def test_movie_detail_view(self):
        movie = Movie.objects.create(
            title="Test Movie",
            release_year=2022,
            director="Test Director",
            runtime=120,
            imdb=7.5,
            country="USA",
            description="Test Description",
            poster_url="https://example.com"
        )
        response = self.client.get(reverse("movies:movie-detail", kwargs={"pk": movie.pk}))
        self.assertEqual(response.status_code, 200)
