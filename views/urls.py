from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
app_name='views'
urlpatterns = [
    path('', TemplateView.as_view(template_name='views/main.html')),
    path('funky', views.funky),
    path('danger', views.danger),
    path('game', views.game),
    path('rest/<int:guess>', views.rest),
    path('bounce', views.bounce),
    path('main', views.MainView.as_view()),
    path('remain/<slug:guess>', views.RestMainView.as_view()),
]

