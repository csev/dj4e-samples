
from django.urls import path
from . import views

# https://stackoverflow.com/questions/30430131/get-the-file-path-for-a-static-file-in-django-code

urlpatterns = [ 

]

import os
from django.urls import re_path
from django.views.static import serve
from django.conf import settings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if settings.DEBUG:
    urlpatterns += [
        re_path(r'^ads/static/(?P<path>.*)$', serve, {
            'document_root': os.path.join(BASE_DIR, 'ads/static'),
        }),
    ]

