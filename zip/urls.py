from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='zip'
urlpatterns = [
    path('', TemplateView.as_view(template_name='zip/main.html'), name='main'),
    path('upload', views.UploadView.as_view(), name='upload'),
]
