from django.shortcuts import get_object_or_404, redirect, render
from .models import MovieStore
from .forms import MovieStoreForm
# Create your views here.

def movie_list(request):
    movies = MovieStore.objects.all()
    return render(request, 'movies/movie_list.html', {'movies': movies})

def movie_create(request):
    if request.method == 'POST':
        form = MovieStoreForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieStoreForm()
    return render(request, 'movies/movie_form.html', {'form': form})

def movie_update(request, pk):
    movie = get_object_or_404(MovieStore, pk=pk)
    if request.method == 'POST':
        form = MovieStoreForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movie_list')
    else:
        form = MovieStoreForm(instance=movie)
    return render(request, 'movies/movie_form.html', {'form': form,'movie':movie})

def movie_delete(request, pk):
    movie = get_object_or_404(MovieStore, pk=pk)
    if request.method == 'POST':
        movie.delete()
        return redirect('movie_list')
    return render(request, 'movies/movie_confirm_delete.html', {'movie': movie})
