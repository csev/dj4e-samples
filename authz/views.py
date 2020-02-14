from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.utils.http import urlencode

class OpenView(View) :
    def get(self, request):
        return render(request, 'authz/main.html')

class ApereoView(View) :
    def get(self, request):
        return render(request, 'authz/main.html')

class ManualProtect(View) :
    def get(self, request):
        if not request.user.is_authenticated :
            loginurl = reverse('login')+'?'+urlencode({'next': request.path})
            return redirect(loginurl)
        return render(request, 'authz/main.html')

class ProtectView(LoginRequiredMixin, View) :
    def get(self, request):
        return render(request, 'authz/main.html')

from django.http import HttpResponse

class DumpPython(View) :
    def get(self, req):
        resp = "<pre>\nUser Data in Python:\n\n"
        resp += "Login url: " + reverse('login') + "\n"
        resp += "Logout url: " + reverse('logout') + "\n\n"
        if req.user.is_authenticated:
            resp += "User: " + req.user.username + "\n"
            resp += "Email: " + req.user.email + "\n"
        else:
            resp += "User is not logged in\n"

        resp += "\n"
        resp += "</pre>\n"
        resp += """<a href="/authz">Go back</a>"""
        return HttpResponse(resp)


# https://docs.djangoproject.com/en/3.0/topics/auth/default/#authentication-in-web-requests

