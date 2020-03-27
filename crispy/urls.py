from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/3.0/topics/http/urls/
app_name='crispy'
urlpatterns = [
    path('', TemplateView.as_view(template_name='crispy/main.html'), name="main"),
    path('boring', views.MyView.as_view(template_name='crispy/boring.html')),
    path('awesome', views.MyView.as_view(template_name='crispy/awesome.html')),
]

