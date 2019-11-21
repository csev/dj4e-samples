from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='jsonsample'
urlpatterns = [
    path('', TemplateView.as_view(template_name='jsonsample/main.html')),
    path('syntax', TemplateView.as_view(template_name='jsonsample/syntax.html'), 
        name='syntax'),
    path('jsonfun', views.jsonfun, name="jsonfun"),
]

