from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='main_home.html')),
    path('helloworld', views.helloworld) ,
]
