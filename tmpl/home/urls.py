from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='main.html')),
    path('simple', views.simple),
    path('guess', views.guess),
    path('special', views.special),
    path('loop', views.loop),
    path('cond', views.cond),
    path('nested', views.nested),
    path('game', views.game),

]

