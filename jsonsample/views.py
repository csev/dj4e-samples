from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
import time

class HomeView(View) :
    def get(self, request):
        return render(request, 'jsonsample/main.html')

def jsonfun(request):
    time.sleep(2)
    stuff = {
        'first': 'first thing',
        'second': 'second thing'
    }
    return JsonResponse(stuff)

class ChatMain(View) :
    def get(self, request):
        return render(request, 'jsonsample/chat.html')


# References

# https://simpleisbetterthancomplex.com/tutorial/2016/07/27/how-to-return-json-encoded-response.html
