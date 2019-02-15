User Model
----------

Take a look at models.py


    $ python3 manage.py makemigrations
    Migrations for 'home':
      home/migrations/0001_initial.py
        - Create model User

    $ git status
    Untracked files:

        home/models.py
        home/migrations/0001_initial.py

    no changes added to commit (use "git add" and/or "git commit -a")

    $ python3 manage.py migrate
    Running migrations:
    Applying contenttypes.0001_initial... OK
    ...
    Applying sessions.0001_initial... OK
    Applying home.0001_initial... OK

    $ sqlite3 db.sqlite3
    SQLite version 3.24.0 2018-06-04 14:10:15
    Enter ".help" for usage hints.
    sqlite> .tables
    auth_group                  django_admin_log
    auth_group_permissions      django_content_type
    auth_permission             django_migrations
    auth_user                   django_session
    auth_user_groups            home_user
    auth_user_user_permissions
    sqlite> .schema home_user
    CREATE TABLE IF NOT EXISTS "home_user" (
        "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT,
        "name" varchar(128) NOT NULL,
        "email" varchar(128) NOT NULL
    );
    sqlite> .quit

    $ python3 manage.py shell
    >>> from home.models import User
    >>> u = User(name='Kristen', email='kf@umich.edu')
    >>> u.save()
    >>> print(u.id)
    1
    >>> print(u.email)
    kf@umich.edu
    >>>

    >>> from django.db import connection
    >>> print(connection.queries)
    [
    {'sql': 'BEGIN', 'time': '0.000'},
    {'sql': 'INSERT INTO "home_user" ("name", "email") VALUES (\'Kristen\', \'kf@umich.edu\')',
        'time': '0.002'}
    ]
    >>>

