from django.shortcuts import render,redirect
from django.views import View

class FirstView(View):  
    def get(self, request) :
        return render(request, 'route/main.html', ctx)

class SecondView(View):  
    def get(self, request) :
        return render(request, 'route/main.html', ctx)


# References

# https://docs.djangoproject.com/en/2.2/topics/http/urls/#topics-http-reversing-url-namespaces

