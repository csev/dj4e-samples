from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
app_name='menu'

urlpatterns = [
    path('', views.TheView.as_view(), name='main'),
    path('page1', views.TheView.as_view(), name='page1'),
    path('page2', views.TheView.as_view(), name='page2'),
    path('page3', views.TheView.as_view(), name='page3'),
]
