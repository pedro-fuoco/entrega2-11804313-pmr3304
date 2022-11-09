from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=255)
    context = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True, blank=True)
    poster_url = models.URLField(max_length=500, blank=True, default='')

    def __str__(self):
        return f'{self.title} ({self.date})'

class Comment(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    likes = models.IntegerField(default=0)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    def __str__(self):
        return f'"{self.text}" - {self.author.username}'

class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    posts = models.ManyToManyField(Post)

    def __str__(self):
        return f'{self.name}'