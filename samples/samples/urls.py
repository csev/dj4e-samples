"""samples URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.urls import include
from django.conf import settings
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', include('home.urls')),  # Keep
    path('admin/', admin.site.urls),  # Keep
    path('accounts/', include('django.contrib.auth.urls')),  # Keep
    # path('ads/', include('ads.urls')),  # Keep

    # Sample applications
    path('hello/', include('hello.urls')),
    path('getpost/', include('getpost.urls')),
    path('users/', include('users.urls')),
    path('tracks/', include('tracks.urls')),
    path('views/', include('views.urls')),
    path('tmpl/', include('tmpl.urls')),
    path('gview/', include('gview.urls')),
    path('route/', include('route.urls', namespace='route')),
    path('session/', include('session.urls')),
    path('form/', include('form.urls')),
    path('crispy/', include('crispy.urls')),
    path('myarts/', include('myarts.urls')),
    path('menu/', include('menu.urls')),
    path('forums/', include('forums.urls')),
    path('pics/', include('pics.urls')),
    path('rest/', include('rest.urls')),
    path('favs/', include('favs.urls')),
]

# Keep everything below this line
if 'social_django' in settings.INSTALLED_APPS :
    urlpatterns += [
        url(r'^oauth/', include('social_django.urls', namespace='social')),
    ]

# Serve the favicon
import os
from django.views.static import serve
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
urlpatterns += [
    path('favicon.ico', serve, {
            'path': 'favicon.ico',
            'document_root': os.path.join(BASE_DIR, 'home/static'),
        }
    ),
]

# References

# https://docs.djangoproject.com/en/2.2/ref/urls/#include

