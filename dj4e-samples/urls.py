"""samples URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
import os
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from django.views.static import serve

urlpatterns = [
    path('', include('home.urls')),  # Change to ads.urls
    path('admin/', admin.site.urls),  # Keep
    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    url(r'^oauth/', include('social_django.urls', namespace='social')),  # Keep

    # Sample applications
    path('hello/', include('hello.urls')),
    path('users/', include('users.urls')),
    path('tracks/', include('tracks.urls')),
    path('views/', include('views.urls')),
    path('route/', include('route.urls', namespace='nsroute')),
    path('tmpl/', include('tmpl.urls')),
    path('gview/', include('gview.urls')),
    path('session/', include('session.urls')),
    path('authz/', include('authz.urls')),
    path('getpost/', include('getpost.urls')),
    path('form/', include('form.urls')),
    path('crispy/', include('crispy.urls')),
    path('myarts/', include('myarts.urls')),
    path('menu/', include('menu.urls')),
    path('forums/', include('forums.urls')),
    path('pics/', include('pics.urls')),
    path('favs/', include('favs.urls')),
    path('favsql/', include('favsql.urls')),
    path('rest/', include('rest.urls')),
    path('autos/', include('autos.urls')),
    path('usermodel/', include('usermodel.urls')),
    path('chat/', include('chat.urls')),
    path('util/', include('util.urls')),
    path('well/', include('well.urls')),
]

# Serve the static HTML
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    url(r'^site/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'site'),
         'show_indexes': True},
        name='site_path'
        ),
]

# Serve the favicon - Keep for later
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

# Switch to social login if it is configured - Keep for later
try:
    from . import github_settings
    social_login = 'registration/login_social.html'
    urlpatterns.insert(0,
                       path('accounts/login/', auth_views.LoginView.as_view(template_name=social_login))
                       )
    print('Using', social_login, 'as the login template')
except:
    print('Using registration/login.html as the login template')

# References

# https://docs.djangoproject.com/en/3.0/ref/urls/#include
