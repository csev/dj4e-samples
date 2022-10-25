from django.shortcuts import render, redirect, reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.humanize.templatetags.humanize import naturaltime
from django.http import JsonResponse, HttpResponse
from chat.models import Message
from datetime import datetime, timedelta
from django.utils.html import escape
import time

class HomeView(View) :
    def get(self, request):
        return render(request, 'chat/main.html')

def jsonfun(request):
    time.sleep(2)
    stuff = {
        'first': 'first thing',
        'second': 'second thing'
    }
    return JsonResponse(stuff)

class TalkMain(LoginRequiredMixin, View) :
    def get(self, request):
        return render(request, 'chat/talk.html')

    def post(self, request) :
        message = Message(text=request.POST['message'], owner=request.user)
        message.save()
        return redirect(reverse('chat:talk'))

class TalkMessages(LoginRequiredMixin, View) :
    def get(self, request):
        # Delete chats from more than 2 hours ago
        Message.objects.filter(created_at__lt=datetime.now()-timedelta(hours=2)).delete()
        messages = Message.objects.all().order_by('-created_at')[:10]
        results = []
        for message in messages:
            # For now we escape in the back-end - but a real application would esacpe in JS
            result = [escape(message.text), naturaltime(message.created_at)]
            results.append(result)
        return JsonResponse(results, safe=False)


# References

# https://simpleisbetterthancomplex.com/tutorial/2016/07/27/how-to-return-json-encoded-response.html
