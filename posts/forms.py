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

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = [
            'author',
            'text',
        ]
        labels = {
            'author': 'Usuário',
            'text': 'Resenha',
        }