"""hello URL Configuration

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

urlpatterns = [
    path('admin/', admin.site.urls),
]

# It is seen as somewhat tacky to have project-wide views.  A better
# practice might be to make an application named "home" that captures
# the "global" pages for the application and then route top level paths
# to that home project.   As a note, while you *can* make project-wide
# views you cannot make project-wide models.

from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
