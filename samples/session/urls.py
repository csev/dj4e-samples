from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='session'
urlpatterns = [
    path('', TemplateView.as_view(template_name='session/main.html')),
    path('cookie', views.cookie),
    path('sessfun', views.sessfun),
]

