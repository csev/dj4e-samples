

from django.db import connection

def print_queries():
    retval = list()
    for i, query in enumerate(connection.queries):
        q = query['sql']
        if q.find('SELECT "django_session"."session_key"') == 0 : continue
        if q.find('SELECT "auth_user"."id", "auth_user"."password"') == 0 : continue
        print(q)
