from gview.models import Cat, Dog, Horse, Car

from django.views import View
from django.shortcuts import render

# Create your views here.

class CatListView(View):
    def get(self, request) :
        stuff = Cat.objects.all()
        cntx = { 'cat_list': stuff }
        return render(request, 'gview/cat_list.html', cntx)
    
class CatDetailView(View):
    def get(self, request, pk_from_url) :
        obj = Cat.objects.get(pk=pk_from_url)
        cntx = { 'cat': obj }
        return render(request, 'gview/cat_detail.html', cntx)

# Lets apply the "DRY" pattern - "Don't Repeat Yourself"
class DogListView(View):
    model = Dog
    def get(self, request) :
        modelname = self.model._meta.verbose_name.title().lower()
        stuff = self.model.objects.all()
        cntx = { modelname+'_list': stuff }
        return render(request, 'gview/'+modelname+'_list.html', cntx)
    
class DogDetailView(View):
    model = Dog
    def get(self, request, pk) :
        modelname = self.model._meta.verbose_name.title().lower()
        obj = self.model.objects.get(pk=pk)
        cntx = { modelname : obj }
        return render(request, 'gview/'+modelname+'_detail.html', cntx)

# Lets save time and use the built-in generics
# https://docs.djangoproject.com/en/2.1/topics/class-based-views/generic-display/
from django.views import generic

class HorseListView(generic.ListView):
    model = Horse

class HorseDetailView(generic.DetailView):
    model = Horse

# Lets review how inheritance works to avoid repeating ourselves
# It is all about convention
class DJ4EListView(View):
    def get(self, request) :
        modelname = self.model._meta.verbose_name.title().lower()
        stuff = self.model.objects.all()
        cntx = { modelname+'_list': stuff }
        return render(request, 'gview/'+modelname+'_list.html', cntx)
    
class DJ4EDetailView(View):
    def get(self, request, pk) :
        modelname = self.model._meta.verbose_name.title().lower()
        obj = self.model.objects.get(pk=pk)
        cntx = { modelname : obj }
        return render(request, 'gview/'+modelname+'_detail.html', cntx)

# Lets reuse those "generic" classes
class CarListView(DJ4EListView):
    model = Car

class CarDetailView(DJ4EDetailView):
    model = Car

# There is much more to learn
# https://docs.djangoproject.com/en/2.1/ref/class-based-views/generic-display/#django.views.generic.detail.DetailView
# https://docs.djangoproject.com/en/2.1/ref/class-based-views/generic-display/#django.views.generic.detail.ListView

