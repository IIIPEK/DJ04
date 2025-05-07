from django.urls import path
from . import views

urlpatterns = [
    path('', views.films_index, name='films_index'),
    path('<int:film_id>/', views.film_detail, name='film_detail'),
    path('add/', views.add_film, name='film_add'),
    ]
