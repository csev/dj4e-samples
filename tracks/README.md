Tracks Model
------------

Take a look at models.py.  Make a superuser

    $ python3 manage.py createsuperuser
    Username (leave blank to use 'csev'): dj4e
    Email address: sample@sample.com
    Password: 
    Password (again): 
    Superuser created successfully.

Sample execution

    $ python3 manage.py shell
    >>> from tracks.models import Artist, Genre, Album, Track;
    >>> zep = Artist(name='Led Zepplin')
    >>> zep.save()
    >>> zep.id
    1
    >>> abc = Artist(name='ACDC')
    >>> abc.save()

    >>> Artist.objects.values()
    <QuerySet [{'id': 1, 'name': 'Led Zepplin'}, {'id': 2, 'name': 'ACDC'}]>

    >>> made = Album(title='Who Made Who', artist=abc)
    >>> made.save()
    >>> zep_iv = Album(title='IV', artist=zep)
    >>> zep_iv.save()
    >>> ROCK = Genre(name='Rock')
    >>> ROCK.save()
    >>> met = Genre(name='Metal')
    >>> met.save()

    >>> x = Track(title='Black Dog', rating=5, length=297, count=9, album=zep_iv, genre=ROCK)
    >>> x.save()
    >>> x.id
    1
    >>> x = Track(title='Stairway', rating=5, length=482, count=0, album=zep_iv, genre=ROCK)
    >>> x.save()
    >>> x.id
    2
    >>> x = Track(title='About to Rock', rating=5, length=313, count=0, album=made, genre=met)
    >>> x.save()
    >>> x = Track(title='Who Made Who', rating=5, length=207, count=0, album=made, genre=met)
    >>> x.save()
    >>>
    >>> Track.objects.values()
    <QuerySet [{'id': 1, 'title': 'Black Dog', 'rating': 5, 'length': 297, 'count': 9,
     'album_id': 2, 'genre_id': 1},
     {'id': 2, 'title': 'Stairway', 'rating': 5, 'length': 482, 'count': 0,
     'album_id': 2, 'genre_id': 1},
     {'id': 3, 'title': 'About to Rock', 'rating': 5, 'length': 313, 'count': 0,
     'album_id': 1, 'genre_id': 2},
     {'id': 4, 'title': 'Who Made Who', 'rating': 5, 'length': 207, 'count': 0,
     'album_id': 1, 'genre_id': 2}]>

    >>> first = Track.objects.get(pk=1)
    >>> first
    <Track: Black Dog>
    >>> print(first)
    Black Dog
    >>> print(first.genre)
    Rock
    >>> print(first.genre.name)
    Rock
    >>>
    >>> print(first.album)
    IV
    >>> print(first.album.artist)
    Led Zepplin
    >>>

    >>> from tracks.models import Artist, Genre, Album, Track;
    >>> x = Artist.objects.get(pk=1)
    >>> x
    <Artist: Led Zepplin>
    >>> x.album_set.values()
    <QuerySet [{'id': 2, 'title': 'IV', 'artist_id': 1}]>

