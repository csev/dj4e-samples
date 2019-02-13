Hello World DJ4E (Using a "home" application)
=============================================

This is a simple single page web application that says "Hello
World".  This puts the "top level" pages in an application called
"home".  

We have to update `home/settings.py` to change the `ALLOWED_HOSTS` and
to pull in the configuration for the new "home" application:

    INSTALLED_APPS = [
        ...
        'django.contrib.staticfiles',
        'home.apps.HomeConfig',
    ]

We delegate the top level URLs to the "home" application in the `home/urls.py` application:

    from django.urls import include
    from home import views

    urlpatterns += [
        path('', include('home.urls')),
    ]

The file `home/urls.py` was created:

    from django.urls import path
    from . import views

    urlpatterns = [
        path('', views.index, name='home'),
    ]

The file `home/views.py` was created:

    from django.http import HttpResponse
    import logging

    logger = logging.getLogger(__name__)

    def index(request):
        logging.error('Hello world DJ4E in the log...')
        print('Hello world DJ4E in a print statement...')
        response = """<html><body><p>Hello world DJ4E in HTML</p>
        </body></html>"""
        return HttpResponse(response)

This sends a log message, does a print statement (later useful for debugging)
and then returns an HTML response.
