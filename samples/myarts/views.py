from myarts.models import Article

from django.views import View
from django.views import generic
from django.shortcuts import render

from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

class ArticleListView(OwnerListView):
    model = Article
    template_name = "article_list.html"

class ArticleDetailView(OwnerDetailView):
    model = Article
    template_name = "article_detail.html"

class ArticleCreateView(OwnerCreateView):
    model = Article
    fields = ['title', 'text']
    template_name = "article_form.html"

class ArticleUpdateView(OwnerUpdateView):
    model = Article
    fields = ['title', 'text']
    template_name = "article_form.html"

class ArticleDeleteView(OwnerDeleteView):
    model = Article
    template_name = "article_delete.html"

