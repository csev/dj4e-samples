from django.urls import path, reverse_lazy
from . import views
from django.views.generic import TemplateView


urlpatterns = [
    path('', views.ThingListView.as_view()),
    path('things', views.RawSQLListView.as_view(), name='things'),
    path('thing/<int:pk>', views.ThingDetailView.as_view(), name='thing_detail'),
    path('thing/create', 
        views.ThingCreateView.as_view(success_url=reverse_lazy('things')), name='thing_create'),
    path('thing/<int:pk>/update', 
        views.ThingUpdateView.as_view(success_url=reverse_lazy('things')), name='thing_update'),
    path('thing/<int:pk>/delete', 
        views.ThingDeleteView.as_view(success_url=reverse_lazy('things')), name='thing_delete'),
]

