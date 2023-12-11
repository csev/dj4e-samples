from django.shortcuts import render
from well.models import Post
from django.views import View
from django.contrib.humanize.templatetags.humanize import naturaltime

from django.db.models import Q

class PostListView(View):
    template_name = "well/list.html"

    def get(self, request) :
        strval =  request.GET.get("search", False)
        if strval :
            # Simple title-only search
            # objects = Post.objects.filter(title__contains=strval).select_related().distinct().order_by('-updated_at')[:10]

            # Multi-field search
            # __icontains for case-insensitive search
            query = Q(title__icontains=strval) 
            query.add(Q(text__icontains=strval), Q.OR)
            post_list = Post.objects.filter(query).select_related().distinct().order_by('-updated_at')[:10]
        else :
            post_list = Post.objects.all().order_by('-updated_at')[:10]

        # Augment the post_list
        for obj in post_list:
            obj.natural_updated = naturaltime(obj.updated_at)

        ctx = {'post_list' : post_list, 'search': strval}
        return render(request, self.template_name, ctx)

# References

# https://docs.djangoproject.com/en/4.2/topics/db/queries/#one-to-many-relationships

# Note that the select_related() QuerySet method recursively prepopulates the
# cache of all one-to-many relationships ahead of time.

# sql “LIKE” equivalent in django query
# https://stackoverflow.com/questions/18140838/sql-like-equivalent-in-django-query

# How do I do an OR filter in a Django query?
# https://stackoverflow.com/questions/739776/how-do-i-do-an-or-filter-in-a-django-query

# https://stackoverflow.com/questions/1074212/how-can-i-see-the-raw-sql-queries-django-is-running
