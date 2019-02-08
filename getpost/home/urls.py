from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dump', views.dump, name='dump'),
    path('guess', views.guess, name='guess'),
]
