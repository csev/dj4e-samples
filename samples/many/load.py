
# python3 manage.py shell < many/load.py

from many.models import Person, Course, Membership

hand = open('many/load.txt')

Person.objects.all().delete()
Course.objects.all().delete()
Membership.objects.all().delete()

# Format
# Jane,I,Python
# Ed,L,Python

for line in hand:
    line = line.strip()
    print(line)
    pieces = line.split(',')
    try:
        p = Person.objects.get(name=pieces[0])
    except:
        print("Inserting person",pieces[0])
        p = Person(name=pieces[0])
        p.save()

    try:
        c = Course.objects.get(name=pieces[2])
    except:
        print("Inserting course",pieces[2])
        c = Course(name=pieces[2])
        c.save()

    r = Membership.LEARNER
    if pieces[1] == 'I' : r = Membership.INSTRUCTOR
    m = Membership(role=r,person=p, course=c)
    m.save()


