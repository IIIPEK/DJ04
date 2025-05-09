from .models import Films
from django.forms import ModelForm, TextInput, Textarea, NumberInput


class FilmsForm(ModelForm):
    class Meta:
        model = Films
        fields = ['title', 'description', 'text', 'rating']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название фильма'}),
            'description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Описание фильма', 'rows': 5}),
            'rating': NumberInput(attrs={'class': 'form-control', 'placeholder': 'Рейтинг фильма','min': '0', 'max': '10', 'default': '0'}),
        }