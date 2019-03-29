from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.PicListView.as_view()),
    path('pics', views.PicListView.as_view(), name='pics'),
    path('pic/<int:pk>', views.PicDetailView.as_view(), name='pic_detail'),
    path('pic/create', 
        views.PicCreateView.as_view(success_url=reverse_lazy('pics')), name='pic_create'),
    path('pic/<int:pk>/update', 
        views.PicUpdateView.as_view(success_url=reverse_lazy('pics')), name='pic_update'),
    path('pic/<int:pk>/delete', 
        views.PicDeleteView.as_view(success_url=reverse_lazy('pics')), name='pic_delete'),
    path('pic_picture/<int:pk>', views.stream_file, name='pic_picture'),

]

