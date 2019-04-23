from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='form'
urlpatterns = [
    path('', TemplateView.as_view(template_name='form/main.html')),
    path('example', views.example),
    path('create', views.SimpleCreate.as_view()),
    path('update', views.SimpleUpdate.as_view()),
    path('validate', views.Validate.as_view()),
    path('success', views.success, name='success'),
]
