from home.models import Cat, Dog, Horse 

from django.views import View
from django.shortcuts import render

# Create your views here.

class CatListView(View):
    def get(self, request) :
        stuff = Cat.objects.all()
        cntx = { 'cat_list': stuff }
        return render(request, 'cat_list.html', cntx)
    
class CatDetailView(View):
    def get(self, request, pk_from_url) :
        obj = Cat.objects.get(pk=pk_from_url)
        cntx = { 'cat': obj }
        return render(request, 'cat_detail.html', cntx)

# Lets rely on built-in generics
from django.views import generic

class HorseListView(generic.ListView):
    model = Horse

class HorseDetailView(generic.DetailView):
    model = Horse
