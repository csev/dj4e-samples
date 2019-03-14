from django.db import models

class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Course(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    LEARNER = 1
    IA = 1000
    GSI = 2000
    INSTRUCTOR = 5000
    ADMIN = 10000

    MEMBER_CHOICES = (
        ( LEARNER, 'Learner'),
        ( IA, 'Instructional Assistant' ),
        ( GSI, 'Grad Student Instructor' ),
        ( INSTRUCTOR, 'Instructor' ),
        ( ADMIN, 'Administrator' ),
    )

    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    
    role = models.IntegerField(
        choices=MEMBER_CHOICES,
        default=LEARNER,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# References

# https://docs.djangoproject.com/en/2.1/topics/db/models/#extra-fields-on-many-to-many-relationships

# https://docs.djangoproject.com/en/2.1/ref/models/fields/#choices

# https://docs.djangoproject.com/en/2.1/topics/db/examples/many_to_many/

# https://docs.djangoproject.com/en/2.1/ref/models/fields/#datefield

