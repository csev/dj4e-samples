from favsql.models import Thing, Fav

from django.views import View
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy

from django.contrib.auth.mixins import LoginRequiredMixin

from myarts.owner import OwnerListView, OwnerDetailView, OwnerCreateView, OwnerUpdateView, OwnerDeleteView

from pprint import pprint

from django.db import connection
import re

class ThingListView(OwnerListView):
    model = Thing
    template_name = "favsql/list.html"

    def get(self, request) :
        thing_list = Thing.objects.all()
        favorites = list()
        if request.user.is_authenticated:
            # rows = [{'id': 2}]  (A list of rows)
            rows = request.user.favsql_favorite_things.values('id')
            favorites = [ row['id'] for row in rows ]
        ctx = {'thing_list' : thing_list, 'favorites': favorites}
        for i, query in enumerate(connection.queries):
            sql = re.split(r'(SELECT|FROM|WHERE|GROUP BY|ORDER BY|INNER JOIN|LIMIT)', query['sql'])
            if not sql[0]: sql = sql[1:]
            sql = [(' ' if i % 2 else '') + x for i, x in enumerate(sql)]
            print('\n### {} ({} seconds)\n\n{};\n'.format(i, query['time'], '\n'.join(sql)))
        return render(request, self.template_name, ctx)

class SQLListView(OwnerListView):
    template_name = "favsql/list_sql.html"

    def get(self, request) :
        if not request.user.is_authenticated:
            thing_list = Thing.objects.all()
        else:
            sql = """SELECT *, favsql_fav.user_id AS FAV_USER_ID FROM favsql_thing
                LEFT JOIN favsql_fav ON favsql_thing.id = favsql_fav.thing_id
                AND favsql_fav.user_id = """ + str(self.request.user.id)
            print(sql)
            thing_list = Thing.objects.raw(sql)
            for obj in thing_list:
                print(obj.owner_id)
            thing_list = Thing.objects.raw(sql)

        for i, query in enumerate(connection.queries):
            sql = re.split(r'(SELECT|FROM|WHERE|GROUP BY|ORDER BY|INNER JOIN|LIMIT)', query['sql'])
            if not sql[0]: sql = sql[1:]
            sql = [(' ' if i % 2 else '') + x for i, x in enumerate(sql)]
            print('\n### {} ({} seconds)\n\n{};\n'.format(i, query['time'], '\n'.join(sql)))
        ctx = {'thing_list' : thing_list}
        return render(request, self.template_name, ctx)

class ThingDetailView(OwnerDetailView):
    model = Thing
    template_name = "favsql/detail.html"

class ThingCreateView(OwnerCreateView):
    model = Thing
    fields = ['title', 'text']
    template_name = "favsql/form.html"
    success_url = reverse_lazy('favsql:things')

class ThingUpdateView(OwnerUpdateView):
    model = Thing
    fields = ['title', 'text']
    template_name = "favsql/form.html"
    # success_url = reverse_lazy('favsql:things')
    success_url = 'http://www.dr-chuck.com/'

class ThingDeleteView(OwnerDeleteView):
    model = Thing
    template_name = "favsql/delete.html"
    success_url = reverse_lazy('favsql:things')

# https://stackoverflow.com/questions/16458166/how-to-disable-djangos-csrf-validation
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.db.utils import IntegrityError

@method_decorator(csrf_exempt, name='dispatch')
class AddFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Add PK",pk)
        t = get_object_or_404(Thing, id=pk)
        fav = Fav(user=request.user, thing=t)
        try:
            fav.save()  # In case of duplicate key
        except IntegrityError as e:
            pass
        return HttpResponse()

@method_decorator(csrf_exempt, name='dispatch')
class DeleteFavoriteView(LoginRequiredMixin, View):
    def post(self, request, pk) :
        print("Delete PK",pk)
        t = get_object_or_404(Thing, id=pk)
        try:
            fav = Fav.objects.get(user=request.user, thing=t).delete()
        except Fav.DoesNotExist as e:
            pass

        return HttpResponse()

