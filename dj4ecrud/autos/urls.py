from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', views.MainView.as_view(), name='autos'),
    path('main/create/', views.AutoCreate.as_view(), name='auto_create'),
    path('main/<int:pk>/update/', views.AutoUpdate.as_view(), name='auto_update'),
    path('main/<int:pk>/delete/', views.AutoDelete.as_view(), name='auto_delete'),
    path('lookup/', views.MakeView.as_view(), name='make_list'),
    path('lookup/create/', views.MakeCreate.as_view(), name='make_create'),
    path('lookup/<int:pk>/update/', views.MakeUpdate.as_view(), name='make_update'),
    path('lookup/<int:pk>/delete/', views.MakeDelete.as_view(), name='make_delete'),
]

