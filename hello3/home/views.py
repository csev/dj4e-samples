from django.http import HttpResponse
from django.views import View

# Create your views here.

# https://docs.djangoproject.com/en/2.1/topics/class-based-views/

class MainView(View) :
    def get(self, request):
        response = """<html><body><p>Hello world MainView in HTML</p>
        <p>This sample code is available at
        <a href="https://github.com/csev/dj4e-samples">
        https://github.com/csev/dj4e-samples</a></p>
        </body></html>"""
        return HttpResponse(response)

