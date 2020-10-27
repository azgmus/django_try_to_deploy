from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea


class ArticlesForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title', 'annons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'название статьи'
            }),
            "annons": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'аннонс'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'дата публикации',

            }),
            "full_text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'текст статьи'
            }),
        }
