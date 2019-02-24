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

urlpatterns = [
    path('', include('home.urls')),
    path('admin/', admin.site.urls),
    path('hello/', include('hello.urls')),
    path('getpost/', include('getpost.urls')),
    path('users/', include('users.urls')),
    path('tracks/', include('tracks.urls')),
    path('views/', include('views.urls')),
    path('templates/', include('templates.urls')),
    path('generic/', include('generic.urls')),
    path('session/', include('session.urls')),
    path('form/', include('form.urls')),
]

if 'crispy_forms' in settings.INSTALLED_APPS :
    urlpatterns += [
        path('crispy/', include('crispy.urls')),
    ]

if 'rest_framework' in settings.INSTALLED_APPS :
    urlpatterns += [
        path('rest/', include('rest.urls')),
    ]

