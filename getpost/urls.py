from django.urls import path
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='getpost/main.html')),
    path('getform', views.getform, name='getform'),
    path('postform', views.postform, name='postform'),
    path('html4', views.html4, name='html4'),
    path('html5', views.html5, name='html5'),
    path('failform', views.failform, name='failform'),
    path('csrfform', views.csrfform, name='csrfform'),
    path('guess', views.guess, name='guess'),
    path('classy', views.ClassyView.as_view(), name='classy'),
    path('bounce', views.bounce, name='bounce'),
    path('awesome', views.AwesomeView.as_view(), name='awesome'),
]
