
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.shortcuts import render, redirect
from django.urls import reverse_lazy

from owner.util import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from meals.models import Meal
from meals.forms import CreateForm

class MealListView(OwnerListView):
    model = Meal
    template_name = "meal_list.html"

class MealDetailView(OwnerDetailView):
    model = Meal
    template_name = "meal_detail.html"

class MealCreateView(LoginRequiredMixin, View):
    template = 'meal_form.html'
    success_url = reverse_lazy('meals')
    def get(self, request) :
        form = CreateForm()
        ctx = { 'form': form }
        return render(request, self.template, ctx)

    def post(self, request) :
        form = CreateForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template, ctx)

        meal = form.save(commit=False)
        meal.owner = self.request.user
        f = self.request.FILES.get('file_data')
        if f:
            bytearr = f.read();
            print('We got a file ',f.name,'size='+str(len(bytearr)),'type='+f.content_type)
            meal.picture = bytearr
            meal.content_type = f.content_type
        meal.save()
        return redirect(self.success_url)

class XMealCreateView(OwnerCreateView):
    model = Meal
    fields = ['title', 'text']
    template_name = "meal_form.html"

    def form_valid(self, form):
        print('views form_valid called')
        object = form.save(commit=False)
        fdata = self.request.FILES.get('file_data')
        if fdata:
            print('We got a file')
        object.save()
        return super(OwnerCreateView, self).form_valid(form)

class MealUpdateView(OwnerUpdateView):
    model = Meal
    fields = ['title', 'text']
    template_name = "meal_form.html"

class MealDeleteView(OwnerDeleteView):
    model = Meal
    template_name = "meal_delete.html"

