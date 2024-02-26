from django.urls import path

from .views import (
    index,
    MovieListView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
    MovieDetailView,
    GenreListView,
    GenreDetailView,
    GenreCreateView,
    GenreUpdateView,
    GenreDeleteView,
    ActorListView,
    ActorDetailView,
    ActorCreateView,
    ActorUpdateView,
    ActorDeleteView
)

urlpatterns = [
    path("", index, name="index"),
    path("movies/", MovieListView.as_view(), name="movie-list"),
    path("movies/<int:pk>/", MovieDetailView.as_view(), name="movie-detail"),
    path(
        "movies/create/",
        MovieCreateView.as_view(),
        name="movie-create",
    ),
    path(
        "movies/<int:pk>/update/",
        MovieUpdateView.as_view(),
        name="movie-update",
    ),
    path(
        "movies/<int:pk>/delete/",
        MovieDeleteView.as_view(),
        name="movie-delete",
    ),
    path("genres/", GenreListView.as_view(), name="genre-list"),
    path("genres/<int:pk>/", GenreDetailView.as_view(), name="genre-detail"),
    path("genres/create/", GenreCreateView.as_view(), name="genre-create"),
    path("genres/<int:pk>/update/", GenreUpdateView.as_view(), name="genre-update"),
    path("genres/<int:pk>/delete/", GenreDeleteView.as_view(), name="genre-delete"),
    path("actors/", ActorListView.as_view(), name="actor-list"),
    path("actors/<int:pk>/", ActorDetailView.as_view(), name="actor-detail"),
    path("actors/create/", ActorCreateView.as_view(), name="actor-create"),
    path("actors/<int:pk>/update/", ActorUpdateView.as_view(), name="actor-update"),
    path("actors/<int:pk>/delete/", ActorDeleteView.as_view(), name="actor-delete"),
]

app_name = "movies"
