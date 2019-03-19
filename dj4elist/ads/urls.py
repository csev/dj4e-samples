from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.AdListView.as_view()),
    path('ads', views.AdListView.as_view(), name='ads'),
    path('ad/<int:pk>', views.AdDetailView.as_view(), name='ad_detail'),
    path('ad/create', 
        views.AdCreateView.as_view(success_url=reverse_lazy('ads')), name='ad_create'),
    path('ad/<int:pk>/update', 
        views.AdUpdateView.as_view(success_url=reverse_lazy('ads')), name='ad_update'),
    path('ad/<int:pk>/delete', 
        views.AdDeleteView.as_view(success_url=reverse_lazy('ads')), name='ad_delete'),
]

