
DJ4E Samples
============

This is a set of Django projects that provide free sample code to
support the www.dj4e.com web site.

You can see some of the samples working at

http://samples.dj4e.com

Setting up a Virtual Environment on the Mac
-------------------------------------------

Install `virtualenv`, if you use homebrew you can:

    brew install virtualenv

Then checkout this repository:

    cd ...wherever...
    git clone https://github.com/csev/dj4e-samples.git
    cd dj4e-samples
    virtualenv .venv
    source .venv/bin/activate
    python --version
    pip install -r requirements4.txt

    python manage.py migrate
    python manage.py createsuperuser --username dj4e-samples
    # python manage.py changepassword dj4e-samples
    # dj4e_nn_!

Running Locally on the Mac
--------------------------

If you have Django installed on your local computer you can test any of the sample
applications by going into the folder and starting the server:

    cd dj4e-samples
    source .venv/bin/activate   # If needed
    python manage.py runserver

And visit `http://localhost:8000`.

Setting up a Virtual Environment on Python Anywhere
---------------------------------------------------

The instructions for setting up a virtual environment on PythonAnywhere in the Linux shell
are:

    mkvirtualenv django4 --python=/usr/bin/python3.11
    pip install django==4.2.3 ## this may take a couple of minutes

To activate the environment type:

    workon django4

Then check this out into some folder:

    cd ~/django_projects    # Create the folder if needed
    git clone https://github.com/csev/dj4e-samples.git
    cd dj4e-samples
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py createsuperuser --username dj4e-samples
    # python manage.py changepassword dj4e-samples
    # dj4e_nn_!
    python manage.py runscript gview_load
    python manage.py runscript many_load

These samples may be updated from time to time so you might want to get updates
using `git pull`.  Also if there are bugs, you are welcome to submit
a Pull Request on github.

All of the documentation material is copyright CC-BY 3.0 and the code is copyright MIT
by whomever wrote the code or documentation.  You are welcome to use this in any way you see
fit and paste code from this repo into your applications.

Running on PythonAnywhere
-------------------------

Once you have checked out the code under `django_projects`, and
ran the migrations and load scripts,
go under the Web tab, update the config files to point to your new application:

    Source code:                /home/--your-account--/django_projects/dj4e-samples
    Working Directory:          /home/--your-account--/django_projects/dj4e-samples

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
your various projects on PythonAnywhere.  Make sure to reload under the Web tab after
every file or configuration change.

