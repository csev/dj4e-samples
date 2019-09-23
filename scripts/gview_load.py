
# In linux, mac terminal, WSL, or PythonAnywhere bash do this 

# python3 manage.py runscript gview_load

# Otherwise make a super user and add the records
# or run the shell and paste the commands.

# https://django-extensions.readthedocs.io/en/latest/runscript.html

from gview.models import Cat, Dog, Horse, Car

x = Cat(name='Sophie')
x.save()
x = Cat(name='Frankie')
x.save()

x = Dog(name='Cutter')
x.save()
x = Dog(name='Peanut')
x.save()

x = Horse(name='Penny')
x.save()
x = Horse(name='Bravo')
x.save()

x = Car(name='SakaiCar')
x.save()
x = Car(name='Subaru')
x.save()
