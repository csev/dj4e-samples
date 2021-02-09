from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView

# namespace:route_name
app_name='tagme'

urlpatterns = [
    path('', views.ForumListView.as_view(), name='all'),
    path('tagme/<int:pk>', views.ForumDetailView.as_view(), name='tagme_detail'),
    path('tagme/create', 
        views.ForumCreateView.as_view(success_url=reverse_lazy('tagme:all')), name='tagme_create'),
    path('tagme/<int:pk>/update', 
        views.ForumUpdateView.as_view(success_url=reverse_lazy('tagme:all')), name='tagme_update'),
    path('tagme/<int:pk>/delete', 
        views.ForumDeleteView.as_view(success_url=reverse_lazy('tagme:all')), name='tagme_delete'),
    path('tagme/<int:pk>/comment', 
        views.CommentCreateView.as_view(), name='tagme_comment_create'),
    path('comment/<int:pk>/delete', 
        views.CommentDeleteView.as_view(success_url=reverse_lazy('tagme:all')), name='tagme_comment_delete'),
]

# We use reverse_lazy in urls.py to delay looking up the view until all the paths are defined

