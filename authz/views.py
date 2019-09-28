# Create your views here.
from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin

class OpenView(View) :
    def get(self, request):
        return render(request, 'authz/open.html')

class ProtectView(LoginRequiredMixin, View) :
    def get(self, request):
        return render(request, 'authz/protect.html')

