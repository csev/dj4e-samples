from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/
urlpatterns = [
    path('', TemplateView.as_view(template_name='main.html')),
    path('cats', views.CatListView.as_view()),
    path('cat/<int:pk_from_url>', views.CatDetailView.as_view()),
    path('dogs', views.DogListView.as_view()),
    path('dog/<int:pk>', views.DogDetailView.as_view()),
    path('horses', views.HorseListView.as_view(), name='horses-all-view'),
    path('horse/<int:pk>', views.HorseDetailView.as_view()),
    path('cars', views.CarListView.as_view(), name='cars'),
    path('car/<int:pk>', views.CarDetailView.as_view(), name='car-detail'),
]

