from django.contrib import admin

# Register your models here.

from forums.models import Forum, Comment

admin.site.register(Forum)
admin.site.register(Comment)
