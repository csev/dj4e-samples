from django.db import models
from django.conf import settings

# Create your models here.

class Message(models.Model) :
    text = models.TextField();
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
