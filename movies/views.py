from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from movies.forms import MovieNameSearchForm, GenreSearchForm, GenreForm, ActorSearchForm, ActorForm
from movies.models import Movie, Actor, Genre

from django_filters.views import FilterView
from .filters import MovieFilter


def index(request):
    context = {
        "num_movies": Movie.objects.count(),
        "num_genres": Genre.objects.count(),
        "num_actors": Actor.objects.count(),
    }

    return render(request, "movies/index.html", context=context)


class MovieListView(FilterView):
    model = Movie
    context_object_name = "movie_list"
    template_name = "movies/movie_list.html"
    filterset_class = MovieFilter
    paginate_by = 24
    queryset = Movie.objects.all()

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
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
            query = form.cleaned_data["title"]
            qs = self.queryset.filter(title__icontains=query)

            # Фільтрація за ім'ям актора
            actor_query = self.request.GET.get("actor", "")
            if actor_query:
                qs = qs.filter(actors__full_name__icontains=actor_query)

            return qs
        return self.queryset


class MovieDetailView(generic.DetailView):
    model = Movie


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


class GenreListView(generic.ListView):
    model = Genre
    paginate_by = 5
    queryset = Genre.objects.all().prefetch_related("movies")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(GenreListView, self).get_context_data(**kwargs)
        name = self.request.GET.get("name", "")
        context["search_form"] = GenreSearchForm(
            initial={
                "name": name
            }
        )
        return context

    def get_queryset(self):
        form = GenreSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                name__icontains=form.cleaned_data["name"]
            )
        return self.queryset


class GenreDetailView(generic.DetailView):
    model = Genre


class GenreCreateView(generic.CreateView):
    model = Genre
    form_class = GenreForm
    success_url = reverse_lazy("movies:genre-list")


class GenreUpdateView(generic.UpdateView):
    model = Genre
    form_class = GenreForm
    success_url = reverse_lazy("movies:genre-list")


class GenreDeleteView(generic.DeleteView):
    model = Genre
    success_url = reverse_lazy("movies:genre-list")


class ActorListView(generic.ListView):
    model = Actor
    paginate_by = 5
    queryset = Actor.objects.all().prefetch_related("movies")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(ActorListView, self).get_context_data(**kwargs)
        full_name = self.request.GET.get("full_name", "")
        context["search_form"] = ActorSearchForm(
            initial={
                "full_name": full_name
            }
        )
        return context

    def get_queryset(self):
        form = ActorSearchForm(self.request.GET)
        if form.is_valid():
            return self.queryset.filter(
                full_name__icontains=form.cleaned_data["full_name"]
            )
        return self.queryset


class ActorDetailView(generic.DetailView):
    model = Actor


class ActorCreateView(generic.CreateView):
    model = Actor
    form_class = ActorForm
    success_url = reverse_lazy("movies:actor-list")


class ActorUpdateView(generic.UpdateView):
    model = Actor
    form_class = ActorForm
    success_url = reverse_lazy("movies:actor-list")


class ActorDeleteView(generic.DeleteView):
    model = Actor
    success_url = reverse_lazy("movies:actor-list")
