
# In linux, mac terminal, WSL, or PythonAnywhere bash do this 

# python3 manage.py runscript gview_load

# Otherwise make a super user and add the records
# or run the shell and paste the commands.

# https://django-extensions.readthedocs.io/en/latest/runscript.html

from gview.models import Cat, Dog, Horse, Car

def run() :
    Cat.objects.all().delete()
    Dog.objects.all().delete()
    Horse.objects.all().delete()
    Car.objects.all().delete()

    x = Cat(name='Sophie')
    x.save()
    x = Cat(name='Frankie')
    x.save()

    x = Dog(name='Shelby')
    x.save()
    x = Dog(name='Luna')
    x.save()

    x = Horse(name='Penny')
    x.save()
    x = Horse(name='Bravo')
    x.save()

    x = Car(name='SakaiCar')
    x.save()
    x = Car(name='Subaru')
    x.save()

    print('gview data loaded')
