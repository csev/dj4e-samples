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

# Lets apply the "DRY" pattern - "Don't Repeat Yourself"
class DogListView(View):
    model = Dog
    def get(self, request) :
        modelname = self.model._meta.verbose_name.title().lower()
        stuff = self.model.objects.all()
        cntx = { modelname+'_list': stuff }
        return render(request, modelname+'_list.html', cntx)
    
class DogDetailView(View):
    model = Dog
    def get(self, request, pk) :
        modelname = self.model._meta.verbose_name.title().lower()
        obj = self.model.objects.get(pk=pk)
        cntx = { modelname : obj }
        return render(request, modelname+'_detail.html', cntx)

# Lets rely on built-in generics
from django.views import generic

class HorseListView(generic.ListView):
    model = Horse

class HorseDetailView(generic.DetailView):
    model = Horse
