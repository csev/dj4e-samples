from django.shortcuts import render
from django.http import HttpResponse

from util.utils import checkguess

# Create your views here.

def guess(request) :
    if checkguess(request) :
        return HttpResponse('Yay!');

    return HttpResponse('Try adding ?guess=nn to the url');

