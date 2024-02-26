from django.urls import path

from .views import (
    index,
    MovieListView,
    MovieCreateView,
    MovieUpdateView,
    MovieDeleteView,
)

urlpatterns = [
    path("", index, name="index"),
    path("movies/", MovieListView.as_view(), name="movie-list"),
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
]

app_name = "movies"