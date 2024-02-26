from django import forms

from movies.models import Movie, Genre, Actor


class MovieNameSearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by name"
            }
        )
    )


class GenreSearchForm(forms.Form):
    name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by genre name"
            }
        )
    )


class GenreForm(forms.ModelForm):
    class Meta:
        model = Genre
        fields = "__all__"


class ActorSearchForm(forms.Form):
    full_name = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by full name"
            }
        )
    )


class ActorForm(forms.ModelForm):
    class Meta:
        model = Actor
        fields = "__all__"
