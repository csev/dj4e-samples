
# python3 manage.py shell < many/load.py

from many.models import Person, Course, Membership

fhand = open('many/load.txt')

Person.objects.all().delete()
Course.objects.all().delete()
Membership.objects.all().delete()

# Format
# jane@tsugi.org,I,Python
# ed@tsugi.org,L,Python

for line in fhand:
    line = line.strip()
    print(line)
    pieces = line.split(',')

    try:
        p = Person.objects.get(email=pieces[0])
    except:
        print("Inserting person",pieces[0])
        p = Person(email=pieces[0])
        p.save()

    try:
        c = Course.objects.get(title=pieces[2])
    except:
        print("Inserting course",pieces[2])
        c = Course(title=pieces[2])
        c.save()

    r = Membership.LEARNER
    if pieces[1] == 'I' : r = Membership.INSTRUCTOR
    m = Membership(role=r,person=p, course=c)
    m.save()


