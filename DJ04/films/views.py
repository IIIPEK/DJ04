from django.shortcuts import render
from .models import Films
from .forms import FilmsForm

# Create your views here.
def films_index(request):


    # Добавляем специфичные данные
    context={
        'page_title': 'Фильмы',
        'page_description': 'Описание всех фильмов.',
        'posts': Films.objects.all(),
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
        form = FilmsForm(request.POST)  # Сюда сохранится информация от пользователя.
        if form.is_valid():
            form.save()
        else:
            error = "Данные были заполнены некорректно"
    form = FilmsForm()
    return render(request, 'films/add_film.html', {'form': form, 'error': error})