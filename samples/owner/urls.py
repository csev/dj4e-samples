from django.urls import path, reverse_lazy
from . import views

urlpatterns = [
    path('', views.ArticleListView.as_view()),
    path('articles', views.ArticleListView.as_view(), name='articles'),
    path('article/<int:pk>', views.ArticleDetailView.as_view(), name='article_detail'),
    path('article/create', 
        views.ArticleCreateView.as_view(success_url=reverse_lazy('articles')), name='article_create'),
    path('article/<int:pk>/update', 
        views.ArticleUpdateView.as_view(success_url=reverse_lazy('articles')), name='article_update'),
    path('article/<int:pk>/delete', 
        views.ArticleDeleteView.as_view(success_url=reverse_lazy('articles')), name='article_delete'),
]

