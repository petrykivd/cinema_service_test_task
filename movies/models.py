from django.db import models


class Actor(models.Model):
    full_name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.full_name

    class Meta:
        ordering = ('full_name',)


class Genre(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_year = models.IntegerField()
    director = models.CharField(max_length=255)
    actors = models.ManyToManyField(Actor, related_name='movies')
    runtime = models.IntegerField()
    imdb = models.FloatField()
    country = models.CharField(max_length=255)
    description = models.TextField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    poster_url = models.URLField()

    def __str__(self):
        return f"{self.id} {self.title}"

    class Meta:
        ordering = ('title',)
