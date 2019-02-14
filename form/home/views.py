from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views import View
from home.forms import BasicForm
from home.library import get_form_errors

from pprint import pprint
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

class SimpleUpdate(DumpPostView):
    def get(self, request) :
        old_data = {
            'title': 'SakaiCar', 
            'mileage' : 42, 
            'purchase_date': '2018-08-14'
        }
        form = BasicForm(old_data)
        ctx = {'form' : form}
        return render(request, 'form.html', ctx)

class SimpleValidate(DumpPostView):
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
        form = BasicForm(request.POST)
        form.is_valid() # We are going to print no matter what...
        js = json.dumps(request.POST, sort_keys=True, indent=4)        
        ctx = {'title': 'request.POST', 'dump': js, 'form': form}
        return render(request, 'formdump.html', ctx)

class RedirectValidate(DumpPostView):
    def get(self, request) :
        # Check if we have been redirected...
        redirect_html = request.session.pop('form_error_html', False)
        if redirect_html : return HttpResponse(redirect_html)

        old_data = {
            'title': 'SakaiCar', 
            'mileage' : 42, 
            'purchase_date': '2018-08-14'
        }
        form = BasicForm(initial=old_data)
        ctx = {'form' : form}
        return render(request, 'form.html', ctx)

    def post(self, request) :
        form = BasicForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            html = render_to_string('form.html', ctx, request=request)
            request.session['form_error_html'] = html
            return redirect(request.path)

        js = json.dumps(request.POST, sort_keys=True, indent=4)        
        ctx = {'title': 'request.POST', 'dump': js}
        return render(request, 'formdump.html', ctx)

# Pass only the errors back in a list
class RedirectValidate2(DumpPostView):
    def get(self, request) :
        old_data = {
            'title': 'SakaiCar', 
            'mileage' : 42, 
            'purchase_date': '2018-08-14'
        }
        old_data = request.session.pop('form_post_data', old_data)
        form_errors = request.session.pop('form_post_errors', False)

        form = BasicForm(initial=old_data)

        ctx = {'form' : form, 'errors': form_errors}
        return render(request, 'formerrors.html', ctx)

    def post(self, request) :
        form = BasicForm(request.POST)
        pprint(form)
        if not form.is_valid() :
            request.session['form_post_data'] = request.POST
            request.session['form_post_errors'] = get_form_errors(form)
            return redirect(request.path)

        js = json.dumps(request.POST, sort_keys=True, indent=4)        
        ctx = {'title': 'request.POST', 'dump': js}
        return render(request, 'formdump.html', ctx)
# References

# https://stackoverflow.com/questions/14647723/django-forms-if-not-valid-show-form-with-error-message
# https://stackoverflow.com/questions/383944/what-is-a-python-equivalent-of-phps-var-dump
