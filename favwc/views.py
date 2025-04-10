from .models import Thing, Fav

from django.views import View
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin

from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

class ThingListView(OwnerListView):
    model = Thing
    template_name = "favwc/list.html"

    def get(self, request) :
        thing_list = Thing.objects.all()
        favorites = list()
        if request.user.is_authenticated:
            # rows = [{'id': 2}, {'id': 4} ... ]  (A list of rows)
            rows = request.user.favwc_favorite_things.values('id')
            print(rows)
            # favorites = [2, 4, ...] using list comprehension
            favorites = [ row['id'] for row in rows ]
        print(favorites)
        ctx = {'thing_list' : thing_list, 'favorites': favorites}
        return render(request, self.template_name, ctx)

class ThingDetailView(OwnerDetailView):
    model = Thing
    template_name = "favwc/detail.html"

class ThingCreateView(OwnerCreateView):
    model = Thing
    fields = ['title', 'text']
    template_name = "favwc/form.html"

class ThingUpdateView(OwnerUpdateView):
    model = Thing
    fields = ['title', 'text']
    template_name = "favwc/form.html"

class ThingDeleteView(OwnerDeleteView):
    model = Thing
    template_name = "favwc/delete.html"

# csrf exemption in class based views
# https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class ToggleFavoriteView(LoginRequiredMixin, View):
    # Add get for manual retrieval
    def get(self, request, pk) :
        t = get_object_or_404(Thing, id=pk)
        try:
            fav = Fav.objects.get(user=request.user, thing=t).delete()
            return HttpResponse("Favorite present: "+str(fav))
        except:
            return HttpResponse("Favorite not present: "+str(t)+" -> "+str(request.user))

    def post(self, request, pk) :
        t = get_object_or_404(Thing, id=pk)
        fav = Fav(user=request.user, thing=t)
        try:
            fav.save()
            return HttpResponse("Favorite added 42")
        except IntegrityError:  # Already there, lets delete...
            Fav.objects.get(user=request.user, thing=t).delete()
            return HttpResponse("Favorite deleted 42")
        return HttpResponse("Something went wrong")
