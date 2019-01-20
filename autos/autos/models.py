
from django.db import models
from django.contrib.auth.models import User

class Make(models.Model):
    """Model representing a book genre."""
    name = models.CharField(max_length=200, help_text='Enter a make (e.g. Dodge)')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

class Auto(models.Model) : 
    nickname = models.CharField(max_length=200)
    make = models.ForeignKey('Make', on_delete=models.CASCADE, null=False)
