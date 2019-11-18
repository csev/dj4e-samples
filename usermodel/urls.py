from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='usermodel'
urlpatterns = [
    path('', views.listusers), 
]

