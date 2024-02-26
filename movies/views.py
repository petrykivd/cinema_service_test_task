from django.shortcuts import render
from django.views import generic

from movies.models import Movie, Actor, Genre


def index(request):
    context = {
        "num_movies": Movie.objects.count(),
        "num_genres": Genre.objects.count(),
        "num_actors": Actor.objects.count(),
    }

    return render(request, "movies/index.html", context=context)


class MovieListView(generic.ListView):
    model = Movie
    paginate_by = 25
