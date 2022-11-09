from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.shortcuts import render
from django.http import HttpResponse
from .temp_data import post_data
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Category
from .forms import PostForm, CommentForm
from django.views import generic
from django.utils import timezone
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView


class PostListView(generic.ListView):
    model = Post
    template_name = 'posts/index.html'

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'posts/detail.html'

class PostCreateView(generic.CreateView):
    model = Post
    template_name = 'posts/create.html'
    fields = ["title", "context", "poster_url"]
    def get_success_url(self):
        return reverse('posts:index')

class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = 'posts/update.html'
    fields = ["title", "context", "poster_url"]
    template_name_suffix = '_update_form'
    def get_success_url(self):
        return reverse('posts:index')

class PostDeleteView(generic.DeleteView):
    model = Post
    template_name = 'posts/delete.html'
    def get_success_url(self):
        return reverse('posts:index')

def search_posts(request):
    context = {}
    if request.GET.get('query', False):
        search_term = request.GET['query'].lower()
        post_list = Post.objects.filter(title__icontains=search_term)
        context = {"post_list": post_list}
    return render(request, 'posts/search.html', context)

def create_comment(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_author = form.cleaned_data['author']
            comment_text = form.cleaned_data['text']
            comment = Comment(author=comment_author,
                            text=comment_text,
                            post=post)
            comment.save()
            return HttpResponseRedirect(
                reverse('posts:detail', args=(post_id, )))
    else:
        form = CommentForm()
    context = {'form': form, 'post': post}
    return render(request, 'posts/comment.html', context)

class CategoryListView(generic.ListView):
    model = Category
    template_name = 'posts/category.html'

class CategoryCreateView(generic.CreateView):
    model = Category
    template_name = 'posts/create_category.html'
    fields = ['name', 'description', 'posts']
    success_url = reverse_lazy('posts:categories')