from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.views import View
from django.urls import reverse
from form.forms import BasicForm
import html

def example(request) :
    form = BasicForm()
    return HttpResponse(form.as_table())

# Call as dumpdata('GET', request.GET)
def dumpdata(place, data) :
    retval = ""
    if len(data) > 0 :
        retval += '<p>Incoming '+place+' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval

class DumpPostView(View):  # Reusable bit...
    def post(self, request) :
        dump = dumpdata('POST', request.POST)
        ctx = {'title': 'request.POST', 'dump': dump}
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
        # If there are no errors, we would save the data
        x = reverse('form:success')
        return redirect(x)

def success(request) :
    return HttpResponse('Thank you!')


# References

# https://stackoverflow.com/questions/383944/what-is-a-python-equivalent-of-phps-var-dump
