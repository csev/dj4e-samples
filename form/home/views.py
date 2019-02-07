from django.shortcuts import render
from django.http import HttpResponse

from home.forms import BasicForm

# Create your views here.

def example(request) :
    form = BasicForm()

    return HttpResponse(form.as_table())
