import django_filters
from .models import Movie, Actor


class MovieFilter(django_filters.FilterSet):
    release_year = django_filters.NumberFilter(field_name='release_year', lookup_expr='exact')
    director = django_filters.CharFilter(field_name='director', lookup_expr='icontains')
    actors = django_filters.ModelMultipleChoiceFilter(field_name='actors', queryset=Actor.objects.all())

    class Meta:
        model = Movie
        fields = []