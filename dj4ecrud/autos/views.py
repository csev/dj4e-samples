from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from autos.models import Auto, Make

# Create your views here.

class MainView(View) :
    def get(self, request):
        do_cleanup(request)  # ignore this :)
        mc = Make.objects.all().count();
        al = Auto.objects.all();

        ctx = { 'make_count': mc, 'auto_list': al };
        return render(request, 'autos/auto_list.html', ctx)

class AutoCreate(LoginRequiredMixin,CreateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos')

class AutoUpdate(LoginRequiredMixin, UpdateView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos')

class AutoDelete(LoginRequiredMixin, DeleteView):
    model = Auto
    fields = '__all__'
    success_url = reverse_lazy('autos')

class MakeView(View) :
    def get(self, request):
        ml = Make.objects.all();
        ctx = { 'make_list': ml };
        return render(request, 'autos/make_list.html', ctx)

class MakeCreate(LoginRequiredMixin,CreateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos')

class MakeUpdate(LoginRequiredMixin, UpdateView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos')

class MakeDelete(LoginRequiredMixin, DeleteView):
    model = Make
    fields = '__all__'
    success_url = reverse_lazy('autos')


# Ignore this - clean out old entries when running on the web
# Clean up if this is running anywhere other than localhost

# https://stackoverflow.com/questions/18622007/runtimewarning-datetimefield-received-a-naive-datetime
# https://stackoverflow.com/questions/10345147/django-query-datetime-for-objects-older-than-5-hours

from datetime import datetime, timedelta
from django.utils import timezone
import datetime

def do_cleanup(request) :
    host = request.META['HTTP_HOST']
    # if host.startswith('128.0.0.1') or host.startswith('localhost') : return
    time_threshold = datetime.datetime.now(tz=timezone.utc) - timedelta(hours=1)
    Auto.objects.filter(created_at=time_threshold).delete()
    Make.objects.filter(created_at=time_threshold).delete()
