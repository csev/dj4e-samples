from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from home.forms import BasicForm

import json

# Create your views here.

def example(request) :
    form = BasicForm()

    return HttpResponse(form.as_table())

class DumpPostView(View):
    def post(self, request) :
        js = json.dumps(request.POST, sort_keys=True, indent=4)        
        ctx = {'title': 'request.POST', 'dump': js}
        return render(request, 'dump.html', ctx)

class SimpleCreate(DumpPostView):
    def get(self, request) :
        form = BasicForm()
        ctx = {'form' : form}
        return render(request, 'form.html', ctx)

class SimpleUpdate(View):
    def get(self, request) :
        old_data = {
            'title': 'SakaiCar', 
            'mileage' : 42, 
            'purchase_date': '2018-08-14'
        }
        form = BasicForm(initial=old_data)
        ctx = {'form' : form}
        return render(request, 'form.html', ctx)

    def post(self, request) :
        js = json.dumps(request.POST, sort_keys=True, indent=4)        
        ctx = {'title': 'request.POST', 'dump': js}
        return render(request, 'dump.html', ctx)
