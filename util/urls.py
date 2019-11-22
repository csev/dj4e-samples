
from django.urls import path
from . import views

app_name='util'
urlpatterns = [
    path('', views.guess)
]

