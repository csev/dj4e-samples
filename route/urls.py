from django.urls import path
from . import views
from django.views.generic import TemplateView

# To make {% url 'route:first-view' %} work in templates
# Also, add namespace in project urls.py 
# Otherwise the name='' values will be global across all applications
app_name = 'route'  

urlpatterns = [
    path('', TemplateView.as_view(template_name='route/main.html')),
    path('first', views.FirstView.as_view(), name='first-view'),
    path('second', views.SecondView.as_view(), name='second-view'),
]

# References

# https://docs.djangoproject.com/en/4.2/topics/http/urls/

# https://docs.djangoproject.com/en/4.2/ref/urls/#include

# https://docs.djangoproject.com/en/4.2/topics/http/urls/#url-namespaces-and-included-urlconfs
