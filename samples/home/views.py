from django.shortcuts import render
from django.views import View
from django.conf import settings

# Create your views here.

class HomeView(View):
    def get(self, request) :
        context = {'installed' : settings.INSTALLED_APPS }
        return render(request, 'main_home.html', context)

