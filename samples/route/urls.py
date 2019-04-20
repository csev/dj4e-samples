from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'route'

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', TemplateView.as_view(template_name='route/main.html')),
    path('first', views.FirstView.as_view(), name='first-view'),
    path('second', views.SecondView.as_view(), name='second-view'),
]

# References

# https://docs.djangoproject.com/en/2.2/ref/urls/#include
