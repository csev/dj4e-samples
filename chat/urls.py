import os
from django.urls import path, re_path
from django.views.static import serve
from . import views
from django.views.generic import TemplateView

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

app_name='chat'
urlpatterns = [
    path('', views.TalkMain.as_view(), name='talk'),
    path('messages', views.TalkMessages.as_view(), name='messages'),

    # Serve up a local static folder to serve spinner.gif
    re_path(r'^static/(?P<path>.*)$', serve,
        {'document_root': os.path.join(BASE_DIR, 'static'), 'show_indexes': True},
        name='static'
    )
]

