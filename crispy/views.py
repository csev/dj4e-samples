from django.shortcuts import render,redirect
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.views import View
from crispy.forms import BasicForm
from django.urls import reverse

from django.contrib import messages

class MyView(View):
    template_name = None # so we can override in urls.py
    def get(self, request) :
        old_data = {
            'title': 'SakaiCar', 
            'mileage' : 42, 
            'purchase_date': '2018-08-14'
        }
        form = BasicForm(initial=old_data)
        ctx = {'form' : form}
        return render(request, self.template_name, ctx)

    def post(self, request) :
        form = BasicForm(request.POST)
        if not form.is_valid() :
            ctx = {'form' : form}
            return render(request, self.template_name, ctx)

        # Save the Data and send a flash!
        messages.add_message(request, messages.SUCCESS, 'Data saved.')
        return redirect(reverse('crispy:main'))

