from django.shortcuts import render, redirect
from .models import Films
from .forms import FilmsForm

# Create your views here.
def films_index(request):


    # Добавляем специфичные данные
    context={
        'page_title': 'Фильмы',
        'page_description': 'Описание всех фильмов.',
        'films': Films.objects.all(),
    }
    return render(request, 'films/index.html', context)

def film_detail(request, film_id):
    film = Films.objects.get(pk=film_id)
    films = Films.objects.all()
    context={
        'page_title': film.title,
        'page_description': film.description,
        'film': film,
        'films': films
    }
    return render(request, 'films/film_detail.html', context)

def add_film(request):
    error = None


    if request.method == 'POST':
        form = FilmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films_index')
        else:
            error = "Проверьте данные"
    form = FilmsForm()
    context = {
        'page_title': 'Добавление нового фильма',
        'page_description': 'Добавьте новый фильм и его описание. Не забудьте оценить его.',
        'form': form,
        'error': error,
    }
    return render(request, 'films/add_film.html', context=context)