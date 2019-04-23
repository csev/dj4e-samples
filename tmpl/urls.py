from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='tmpl'
urlpatterns = [
    path('', TemplateView.as_view(template_name='tmpl/main.html')),
    path('simple', views.simple),
    path('guess', views.guess),
    path('special', views.special),
    path('loop', views.loop),
    path('cond', views.cond),
    path('nested', views.nested),
    path('game/<slug:guess>', views.GameView.as_view()),
    path('game2/<slug:guess>', views.Game2View.as_view()),

]

