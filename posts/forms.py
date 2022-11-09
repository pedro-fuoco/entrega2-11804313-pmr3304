from django.forms import ModelForm
from .models import Post, Review


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = [
            'title',
            'context',
            'poster_url',
        ]
        labels = {
            'title': 'Título',
            'context': 'Texto do post',
            'poster_url': 'URL do Poster',
        }

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Resenha',
        }