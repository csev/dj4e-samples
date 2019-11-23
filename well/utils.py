from django.db import connection

# https://stackoverflow.com/questions/1074212/how-can-i-see-the-raw-sql-queries-django-is-running
def dump_queries() :
    qs = connection.queries
    for q in qs:
        print(q)

