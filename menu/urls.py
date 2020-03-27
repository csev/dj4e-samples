from django.urls import path
from django.views.generic import TemplateView

app_name='menu'
urlpatterns = [
    path('', TemplateView.as_view(template_name='menu/main_menu.html'), name='main'),
    path('page1', TemplateView.as_view(template_name='menu/main_menu.html'), name='page1'),
    path('page2', TemplateView.as_view(template_name='menu/main_menu.html'), name='page2'),
    path('page3', TemplateView.as_view(template_name='menu/main_menu.html'), name='page3'),
]
