
DJ4E Samples
============

This is a set of Django projects that provide free sample code to
support the www.dj4e.com web site.

You can seem some of the samples at

http://samples.dj4e.com

To set this up, simply check it out into some folder

    cd ...wherever...
    git clone https://github.com/csev/dj4e-samples.git

These samples may be updated from time to tims so you might want to get updates
using `git pull`.  Also if there are bugs, you are welcome to submit
a Pull Request on github.

All of the documentation material is copyright CC-BY 3.0 and the code is copyright MIT
by whomever wrote the code or documentation.  You are welcome to use this in any way you see
fit and paste code from this repo into your applications.

Running Locally
---------------

If you have Django installed on your local computer you can test any of the sample
applications bygoing into the folder and starting the server:

    cd dj4e-samples
    python3 manage.py migrate
    python3 manage.py runserver

And visit `http://localhost:8000`.

Running on PythonAnywhere
-------------------------

If you are using PythonAnywhere.com to run your Django applications, you
can check all the sample code out as follows:

    cd ~
    git clone https://github.com/csev/dj4e-samples.git

Then under the Web tab, update the config files to point to your new application:

    Source code:                /home/--your-account--/dj4e-samples
    Working Directory:          /home/--your-account--/dj4e-samples

Use this as your `WGSI configuration file`:

    import os
    import sys

    path = os.path.expanduser('~/django_projects/dj4e-samples')
    if path not in sys.path:
        sys.path.insert(0, path)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'dj4e-samples.settings'
    from django.core.wsgi import get_wsgi_application
    from django.contrib.staticfiles.handlers import StaticFilesHandler
    application = StaticFilesHandler(get_wsgi_application())

You can edit these files and settings in the Web tab to switch between
your various projects on PythonAnywhere.  Make sure to reload after
every flie or configuration change.

