from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from form.forms import BasicForm

from pprint import pprint
import json

# Create your views here.
def example(request) :
    form = BasicForm()
    return HttpResponse(form.as_table())

class DumpPostView(View):  # Reusable bit...
    def post(self, request) :
        js = json.dumps(request.POST, sort_keys=True, indent=4)        
        ctx = {'title': 'request.POST', 'dump': js}
        return render(request, 'form/dump.html', ctx)

class SimpleCreate(DumpPostView): 
    def get(self, request) :
        form = BasicForm()
        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)

class SimpleUpdate(DumpPostView):
    def get(self, request) :
        old_data = {
            'title': 'SakaiCar', 
            'mileage' : 42, 
            'purchase_date': '2018-08-14'
        }
        form = BasicForm(old_data)
        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)

class Validate(DumpPostView):
    def get(self, request) :
        old_data = {
            'title': 'SakaiCar', 
            'mileage' : 42, 
            'purchase_date': '2018-08-14'
        }
        form = BasicForm(initial=old_data)
        ctx = {'form' : form}
        return render(request, 'form/form.html', ctx)

    def post(self, request) :
        form = BasicForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, 'form/form.html', ctx)
        # Save the Data
        # Look up the url for the next view in urls.py
        x = reverse('form:success')
        return redirect(x)

def success(request) :
    return HttpResponse('Thank you!')


# References

# https://stackoverflow.com/questions/383944/what-is-a-python-equivalent-of-phps-var-dump
