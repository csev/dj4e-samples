from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name='authz'
urlpatterns = [
    path('', TemplateView.as_view(template_name='authz/base.html')),
    path('open', views.OpenView.as_view(), name='open'),
    path('protect', views.ProtectView.as_view(), name='protect'),
]
