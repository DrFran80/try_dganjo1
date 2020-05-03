# Create your views here.
from django.http import Http404
from django.urls import reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    CreateView,
    DetailView,
    ListView, 
    UpdateView, 
    DeleteView,
)

from .models import Article
from .forms import ArticleModelForm

class ArticleCreateView(CreateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all() #<blog>/<modelname>_list.html

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

class ArticleUpdateView(UpdateView):
    template_name = 'articles/article_create.html'
    form_class = ArticleModelForm
    queryset = Article.objects.all() #<blog>/<modelname>_list.html

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404( Article, id = id_)

class ArticleDetailView(DetailView):
    template_name = 'articles/article_detail.html'
    queryset = Article.objects.all() #<blog>/<modelname>_list.html

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404( Article, id = id_)

class ArticleListView(ListView):
    template_name = 'articles/article_list.html'
    queryset = Article.objects.all() #<blog>/<modelname>_list.html

class ArticleDeleteView(DeleteView):
    template_name = 'articles/article_delete.html'
    #queryset = Article.objects.all() #<blog>/<modelname>_list.html

    def get_object(self):
        id_ = self.kwargs.get('pk')
        return get_object_or_404( Article, id = id_)
    
    def get_success_url(self):
        return reverse('blog:article-list')