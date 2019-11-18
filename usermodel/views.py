from django.shortcuts import render

from django.contrib.auth.models import User

# https://wsvincent.com/django-referencing-the-user-model/
def listusers(request) :
    ulist = User.objects.all()
    ctx = { 'ulist' : ulist}
    return render(request, 'usermodel/list.html', ctx)

