
import csv  # https://docs.python.org/3/library/csv.html

# python3 manage.py shell < many/load.py

from many.models import Person, Course, Membership

fhand = open('many/load.csv')
reader = csv.reader(fhand)

Person.objects.all().delete()
Course.objects.all().delete()
Membership.objects.all().delete()

# Format
# jane@tsugi.org,I,Python
# ed@tsugi.org,L,Python

for row in reader:
    print(row)

    try:
        p = Person.objects.get(email=row[0])
    except:
        print("Inserting person",row[0])
        p = Person(email=row[0])
        p.save()

    try:
        c = Course.objects.get(title=row[2])
    except:
        print("Inserting course",row[2])
        c = Course(title=row[2])
        c.save()

    r = Membership.LEARNER
    if row[1] == 'I' : r = Membership.INSTRUCTOR
    m = Membership(role=r,person=p, course=c)
    m.save()


