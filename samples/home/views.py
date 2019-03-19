from django.shortcuts import render
from django.views import View
from django.conf import settings


# Create your views here.

class HomeView(View):
    def get(self, request) :
        cleanup()
        print(request.get_host())
        host = request.get_host()
        islocal = host.find('localhost') >= 0 or host.find('127.0.0.1') >= 0
        context = {
            'installed' : settings.INSTALLED_APPS,
            'islocal' : islocal
        }
        return render(request, 'main_home.html', context)

# Remove articles > 30 minutes old
from owner.models import Article
from datetime import timedelta
from django.utils import timezone

# https://stackoverflow.com/questions/37607411/django-runtimewarning-datetimefield-received-a-naive-datetime-while-time-zon/37607525
def cleanup() :
    time_threshold = timezone.now() - timedelta(minutes=30)
    count = Article.objects.filter(created_at__lt=time_threshold).count()
    if count > 1 :
        Article.objects.filter(created_at__lt=time_threshold).delete()
        print('Deleted',count,' expired articles')
