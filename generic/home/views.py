from home.models import Cat, Dog, Horse 

from django.shortcuts import render

# Create your views here.

from django.views import generic

class HorseListView(generic.ListView):
    model = Horse

class HorseDetailView(generic.DetailView):
    model = Horse
