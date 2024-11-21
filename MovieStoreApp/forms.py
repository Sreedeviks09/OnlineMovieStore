from django import forms
from .models import MovieStore

class MovieStoreForm(forms.ModelForm):
    class Meta:
        model= MovieStore
        fields = ['title', 'desc', 'release_date', 'rating', 'image']