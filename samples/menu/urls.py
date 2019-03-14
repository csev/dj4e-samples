from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', views.TheView.as_view(), name='menu_main'),
    path('page1', views.TheView.as_view(), name='menu_page1'),
    path('page2', views.TheView.as_view(), name='menu_page2'),
    path('page3', views.TheView.as_view(), name='menu_page3'),
]
