from django.views import View
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin

from django.core.files.uploadedfile import InMemoryUploadedFile

from owner.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from meals.models import Meal
from meals.forms import CreateForm

class MealListView(OwnerListView):
    model = Meal
    template_name = "meal_list.html"

class MealDetailView(OwnerDetailView):
    model = Meal
    template_name = "meal_detail.html"

# This will handle create and update with an optional pk parameter on get and post
class MealFormView(LoginRequiredMixin, View):
    template = 'meal_form.html'
    success_url = reverse_lazy('meals')
    def get(self, request, pk=None) :
        if not pk : 
            form = CreateForm()
        else: 
            meal = get_object_or_404(Meal, id=pk, owner=self.request.user)
            form = CreateForm(instance=meal)
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request, pk=None) :
        if not pk:
            form = CreateForm(request.POST, request.FILES or None)
        else:
            meal = get_object_or_404(Meal, id=pk, owner=self.request.user)
            form = CreateForm(request.POST, request.FILES or None, instance=meal)

        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        # Adjust the model before saving
        meal = form.save(commit=False)
        meal.owner = self.request.user
       
        # The meal.picture can be one of three things
        # If this is a create and a picture was not chosen, it is None
        # If this is an update and with no prior picture and a new picture was not chosen, it is None
        # If this is an update and with a prior picture and a new picture was not chosen, it is bytes
        # If a picture was uploaded, it is a django.core.files.uploadedfile.InMemoryUploadedFile

        f = meal.picture  
        if isinstance(f, InMemoryUploadedFile):  # Pull out the elements we need
            bytearr = f.read();
            print('Received a file ',f.name,'size='+str(len(bytearr)),'type='+f.content_type)
            meal.picture = bytearr
            meal.content_type = f.content_type

        meal.save()
        return redirect(self.success_url)

class MealDeleteView(OwnerDeleteView):
    model = Meal
    template_name = "meal_delete.html"


def stream_file(request, pk) :
    meal = get_object_or_404(Meal, id=pk)
    response = HttpResponse()
    response['Content-Type'] = meal.content_type
    response['Content-Length'] = len(meal.picture)
    response.write(meal.picture)
    return response

