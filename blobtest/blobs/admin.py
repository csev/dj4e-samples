from django.contrib import admin

# Register your models here.

from blobs.models import Blob, File

admin.site.register(Blob)
admin.site.register(File)
