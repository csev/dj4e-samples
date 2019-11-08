import os
from django.conf.urls import url
from django.views.static import serve

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# All the urls in this application go straight to the static folder
urlpatterns = [
    url(r'^(?P<path>.*)$', serve, 
        {'document_root': os.path.join(BASE_DIR, 'static'), 'show_indexes': True}
    )
]
