from django.db import models
from django.core.validators import MinLengthValidator
from django.contrib.auth.models import User
from django.conf import settings

class Thing(models.Model) :
    title = models.CharField(
            max_length=200,
            validators=[MinLengthValidator(2, "Title must be greater than 2 characters")]
    )
    text = models.TextField()
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(settings.AUTH_USER_MODEL,
        through='Favs', related_name='favorite_things')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # Shows up in the admin list
    def __str__(self):
        return self.title

class Favs(models.Model) :

    thing = models.ForeignKey(Thing, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    # https://docs.djangoproject.com/en/2.1/ref/models/options/#unique-together
    class Meta:
        unique_together = ('thing', 'user')

    def __str__(self) :
        return '%s %s'%(self.thing.title, self.thing.username)
