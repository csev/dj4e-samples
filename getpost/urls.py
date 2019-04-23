from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dump', views.dump, name='dump'),
    path('block', views.block, name='block'),
    path('simple', views.simple, name='simple'),
    path('guess', views.guess, name='guess'),
    path('bounce', views.bounce, name='bounce'),
]
