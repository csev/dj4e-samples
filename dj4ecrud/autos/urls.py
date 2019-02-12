from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', TemplateView.as_view(template_name='autos/index.html')),
    # path('cats', views.CatListView.as_view()),
    # path('cat/<int:pk_from_url>', views.CatDetailView.as_view()),
]

