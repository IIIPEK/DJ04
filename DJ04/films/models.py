from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Films(models.Model):
    title = models.CharField('Title', max_length=200)
    description = models.CharField('Description', max_length=200)
    text = models.TextField('Text')
    created_at = models.DateTimeField('Created', auto_now_add=True)
    updated_at = models.DateTimeField('Updated', auto_now=True)
    rating = models.IntegerField('Raiting', default=0)
    class Meta:
        verbose_name = "Фильм"
        verbose_name_plural = "Фильмы"