from django.shortcuts import render
from django.urls import reverse
from django.views import View

class FirstView(View):  
    def get(self, request) :
        return render(request, 'route/main.html')

class SecondView(View):  
    def get(self, request) :
        u = reverse('gview:cats')
        u2 = reverse('gview:dogs')
        u3 = reverse('gview:dog', args=['42'] )
        ctx = {'x1' : u, 'x2': u2, 'x3': u3 }
        return render(request, 'route/second.html', ctx)

# References

# https://docs.djangoproject.com/en/4.2/topics/http/urls/#topics-http-reversing-url-namespaces

