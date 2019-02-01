from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='main.html')),
    path('funky', views.funky),
    path('danger', views.danger),
    path('game', views.game),
    path('bounce', views.bounce),
    path('main', views.MainView.as_view()),
]

