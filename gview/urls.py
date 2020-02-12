from django.urls import path
from . import views
from django.views.generic import TemplateView

# https://docs.djangoproject.com/en/3.0/topics/http/urls/

# To make {% url 'gview:cats' %} work in templates
# Also, add namespace in project urls.py

app_name = 'gview'

# Note use of plural for list view and singular for detail view
urlpatterns = [
    path('', TemplateView.as_view(template_name='gview/main.html')),
    path('cats', views.CatListView.as_view(), name='cats'),
    path('cat/<int:pk_from_url>', views.CatDetailView.as_view(), name='cat'),
    path('dogs', views.DogListView.as_view(), name='dogs'),
    path('dog/<int:pk>', views.DogDetailView.as_view(), name='dog'),
    path('horses', views.HorseListView.as_view(), name='horses'),
    path('horse/<int:pk>', views.HorseDetailView.as_view(), name='horse'),
    path('cars', views.CarListView.as_view(), name='cars'),
    path('car/<int:pk>', views.CarDetailView.as_view(), name='car'),
    path('wacky', views.WackyEquinesView.as_view(), name='whatever'),
]

