from favs.models import Thing

from django.views import View
from django.views import generic
from django.shortcuts import render

from owner.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

class ThingListView(OwnerListView):
    model = Thing
    template_name = "favs/list.html"

class ThingDetailView(OwnerDetailView):
    model = Thing
    template_name = "favs/detail.html"

class ThingCreateView(OwnerCreateView):
    model = Thing
    fields = ['title', 'text']
    template_name = "favs/form.html"

class ThingUpdateView(OwnerUpdateView):
    model = Thing
    fields = ['title', 'text']
    template_name = "favs/form.html"

class ThingDeleteView(OwnerDeleteView):
    model = Thing
    template_name = "favs/delete.html"

