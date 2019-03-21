from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.ForumListView.as_view()),
    path('forums', views.ForumListView.as_view(), name='forums'),
    path('forum/<int:pk>', views.ForumDetailView.as_view(), name='forum_detail'),
    path('forum/create', 
        views.ForumCreateView.as_view(success_url=reverse_lazy('forums')), name='forum_create'),
    path('forum/<int:pk>/update', 
        views.ForumUpdateView.as_view(success_url=reverse_lazy('forums')), name='forum_update'),
    path('forum/<int:pk>/comment', 
        views.CommentCreateView.as_view(), name='comment_create'),
    path('forum/<int:pk>/delete', 
        views.ForumDeleteView.as_view(success_url=reverse_lazy('forums')), name='forum_delete'),
    path('comment/<int:pk>/delete', 
        views.CommentDeleteView.as_view(success_url=reverse_lazy('forums')), name='comment_delete'),
]

