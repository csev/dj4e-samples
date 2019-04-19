from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/2.1/topics/http/urls/

# By conventions, we prefix all the name= values with the application
# name because they are global across all Django applications in a Django project

urlpatterns = [
    path('', TemplateView.as_view(template_name='gview/main.html')),
    path('cats', views.CatListView.as_view(), name='gview_cats'),
    path('cat/<int:pk_from_url>', views.CatDetailView.as_view(), name='gview_cat'),
    path('dogs', views.DogListView.as_view(), name='gview_dogs'),
    path('dog/<int:pk>', views.DogDetailView.as_view(), name='gview_dog'),
    path('horses', views.HorseListView.as_view(), name='gview_horses'),
    path('horse/<int:pk>', views.HorseDetailView.as_view(), name='gview_horse'),
    path('cars', views.CarListView.as_view(), name='gview_cars'),
    path('car/<int:pk>', views.CarDetailView.as_view(), name='gview_car_detail'),
]

