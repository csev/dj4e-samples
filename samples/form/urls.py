from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', TemplateView.as_view(template_name='main_form.html')),
    path('example', views.example),
    path('create', views.SimpleCreate.as_view()),
    path('update', views.SimpleUpdate.as_view()),
    path('validate', views.Validate.as_view()),
]
