from favs.models import Thing, Fav

from django.views import View
from django.views import generic
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin

from django.db.models import Exists, OuterRef

# These are experimental views - under construction...

class ExistsListView(OwnerListView):
    template_name = "favs/expsql.html"
    def get(self, request) :
        if not request.user.is_authenticated:
            thing_list = Thing.objects.all()
        else:
            thing_list = Thing.objects.annotate(
                FAV_USER_ID=Exists(Fav.objects.filter(user=self.request.user,thing_id=OuterRef('id')))
                ).all()
        ctx = {'thing_list' : thing_list}
        return render(request, self.template_name, ctx)

# https://stackoverflow.com/questions/2314920/django-show-log-orm-sql-calls-from-python-shell
# pip install django-extensions
# ./manage.py shell_plus --print-sql

# Below this line, we see raw sql...   With great power comes great responsibility
# https://docs.djangoproject.com/en/4.2/topics/db/sql/

# A List view using raw SQL - super efficient
class RawSQLListView(OwnerListView):
    template_name = "favs/expsql.html"

    def get(self, request) :
        if not request.user.is_authenticated:
            thing_list = Thing.objects.all()
        else:
            sql = """SELECT *, favs_fav.user_id AS FAV_USER_ID FROM favs_thing
                LEFT JOIN favs_fav ON favs_thing.id = favs_fav.thing_id
                AND favs_fav.user_id = """ + str(self.request.user.id)
            print(sql)
            thing_list = Thing.objects.raw(sql)
        ctx = {'thing_list' : thing_list}
        return render(request, self.template_name, ctx)

# Notes from the shell:
# sql = "SELECT *, favs_fav.user_id AS FAV_USER_ID FROM favs_thing LEFT JOIN favs_fav ON favs_thing.id = favs_fav.thing_id AND favs_fav.user_id = 1"
# thing_list2 = Thing.objects.raw(sql)
# row0 = thing_list2[0]
# row0.FAV_USER_ID
# row1 = thing_list2[1]
# row1.FAV_USER_ID

