import os
from django.urls import path, re_path
from django.views.static import serve
from . import views
from django.views.generic import TemplateView

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app_name='ajax'
urlpatterns = [
    path('', views.HomeView.as_view(), name='main'),
    path('syntax', TemplateView.as_view(template_name='ajax/syntax.html'), 
        name='syntax'),
    path('async', TemplateView.as_view(template_name='ajax/async.html'), 
        name='async'),
    path('promise', TemplateView.as_view(template_name='ajax/promise.html'), 
        name='promise'),
    path('jsonfun', views.jsonfun, name='jsonfun'),

]

