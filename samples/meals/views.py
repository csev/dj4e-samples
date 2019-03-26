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
# We don't use the Generic or OwnerGeneric because (a) we need a form with a file
# and (b) we need to to populate the model with request.FILES
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

        # Adjust the model owner before saving
        meal = form.save(commit=False)
        meal.owner = self.request.user
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

