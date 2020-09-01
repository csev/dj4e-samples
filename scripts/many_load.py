import csv  # https://docs.python.org/3/library/csv.html

# https://django-extensions.readthedocs.io/en/latest/runscript.html

# python3 manage.py runscript many_load

from many.models import Person, Course, Membership


def run():
    fhand = open('many/load.csv')
    reader = csv.reader(fhand)
    next(reader)  # Advance past the header

    Person.objects.all().delete()
    Course.objects.all().delete()
    Membership.objects.all().delete()

    # Format
    # email,role,course
    # jane@tsugi.org,I,Python
    # ed@tsugi.org,L,Python

    for row in reader:
        print(row)

        p, created = Person.objects.get_or_create(email=row[0])
        c, created = Course.objects.get_or_create(title=row[2])

        r = Membership.LEARNER
        if row[1] == 'I':
            r = Membership.INSTRUCTOR
        m = Membership(role=r, person=p, course=c)
        m.save()
