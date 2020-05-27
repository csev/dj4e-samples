from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView

app_name = 'favsql'

urlpatterns = [
    path('', views.ThingListView.as_view(), name='things'),
    path('sql/', views.SQLListView.as_view(), name='thingsql'),
    path('thing/<int:pk>', views.ThingDetailView.as_view(), name='thing_detail'),
    path('thing/create', 
        views.ThingCreateView.as_view(success_url=reverse_lazy('favsql:things')), name='thing_create'),
    path('thing/<int:pk>/update', 
        views.ThingUpdateView.as_view(success_url=reverse_lazy('favsql:things')), name='thing_update'),
    path('thing/<int:pk>/delete', 
        views.ThingDeleteView.as_view(success_url=reverse_lazy('favsql:things')), name='thing_delete'),
    path('thing/<int:pk>/favorite', 
        views.AddFavoriteView.as_view(), name='thing_favorite'),
    path('thing/<int:pk>/unfavorite', 
        views.DeleteFavoriteView.as_view(), name='thing_unfavorite'),
]

