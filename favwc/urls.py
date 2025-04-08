from django.urls import path, reverse_lazy
from . import views

# In urls.py reverse_lazy('favwc:all')
# In views.py class initialization reverse_lazy('favwc:all')
# In views.py methods reverse('favwc:all')
# In templates {% url 'favwc:thing_update' thing.id %}

app_name='favwc'
urlpatterns = [
    path('', views.ThingListView.as_view(), name='all'),
    path('thing/<int:pk>', views.ThingDetailView.as_view(), name='thing_detail'),
    path('thing/create',
        views.ThingCreateView.as_view(success_url=reverse_lazy('favwc:all')), name='thing_create'),
    path('thing/<int:pk>/update',
        views.ThingUpdateView.as_view(success_url=reverse_lazy('favwc:all')), name='thing_update'),
    path('thing/<int:pk>/delete',
        views.ThingDeleteView.as_view(success_url=reverse_lazy('favwc:all')), name='thing_delete'),
    path('thing/<int:pk>/toggle',
        views.ToggleFavoriteView.as_view(), name='thing_toggle'),
]

