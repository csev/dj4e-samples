from django.shortcuts import render
from django.views import View

# Create your views here.

class TheView(View) :
    def get(self, request) :
        x = { 'request' : request }
        return render(request, 'main_menu.html', x)
