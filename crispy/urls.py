from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
app_name='crispy'
urlpatterns = [
    path('', TemplateView.as_view(template_name='crispy/main.html'), name="crispy_main"),
    path('validate', views.Validate.as_view()),
]

