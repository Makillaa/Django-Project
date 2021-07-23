from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput


class ArticlesForm(ModelForm):  # Создание формы и подсоединение её к таблице
    class Meta:
        model = Articles  # Название таблицы
        fields = ['title', 'anons', 'full_text', 'date']  # Поля таблицы

        widgets = {
            'title': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article title'
            }),
            'anons': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article announcement'
            }),
            'date': DateTimeInput(attrs={
                'type': 'date',
                'class': 'form-control',
                'placeholder': 'Date of publication'
            }),
            'full_text': TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Article text'
            }),
        }
