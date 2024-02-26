from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from movies.forms import MovieNameSearchForm
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
    context_object_name = "movie_list"
    template_name = "movies/movie_list.html"
    paginate_by = 24
    queryset = Movie.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(MovieListView, self).get_context_data(**kwargs)
        title = self.request.GET.get("title", "")
        context["search_form"] = MovieNameSearchForm(
            initial={
                "title": title
            }
        )
        return context

    def get_queryset(self):
        form = MovieNameSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                title__icontains=form.cleaned_data["title"]
            )
        return self.queryset


class MovieCreateView(generic.CreateView):
    model = Movie
    fields = "__all__"
    success_url = reverse_lazy("movies:movie-list")


class MovieUpdateView(generic.UpdateView):
    model = Movie
    fields = "__all__"
    success_url = reverse_lazy("movies:movie-list")


class MovieDeleteView(generic.DeleteView):
    model = Movie
    success_url = reverse_lazy("movies:movie-list")
