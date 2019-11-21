from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='jsonsample'
urlpatterns = [
    path('', views.HomeView.as_view()),
    path('syntax', TemplateView.as_view(template_name='jsonsample/syntax.html'), 
        name='syntax'),
    path('jsonfun', views.jsonfun, name='jsonfun'),
    path('chat', views.ChatMain.as_view()),
    # path('messages', views.messages, name='messages')
]

