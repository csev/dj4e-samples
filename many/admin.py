from django.contrib import admin

# Register your models here.

from many.models import Person, Course, Membership

admin.site.register(Person)
admin.site.register(Course)
admin.site.register(Membership)
