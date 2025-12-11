
DJ4E Samples
============

This is a set of Django projects that provide free sample code to
support the www.dj4e.com web site.

You can see some of the samples working at

http://samples.dj4e.com

Setting up a Virtual Environment
--------------------------------

If your prompt looks as follows, it means you have set up a Django 4.2
environment you need to either switch to and/or set up your Django 5.2 environment.

    (django42) 14:58 ~ $

First lets try to switch to Django 5.2 to see if it is already installed with the following
command.

    source ~/.ve52/bin/activate

If you have a Django 5.2 environment your prompt will change to look like:

    (.ve52) 14:15 ~ $

Yay, you do not need to install a virtual environment, you can skip ahead
to "Installing the Sample Code for DJ4E".


Installing a Django 5.2 Virtual Environment
-------------------------------------------

If after all the above checks, you do not have a Django 5.2 virtual environment installed,
lets install one.  First lets make sure your shell has no current virtual environment
by de-activating any current virtual environment:

    cd ~
    deactivate  # May fail - this is OK

If the deactivate fails with the following message - that is OK.  You just were
not in a virtual environment:

    bash: deactivate: command not found

Now lets install a new virtual environment in your home directory (~) with a version of Python
that supports Django 5.2.  The Python version should be 3.10 - 3.13 with a preference toward
the later releases.

You can figure out figure out exactly which versions of Python are available in your
Linux shell (a.k.a. PythonAnywhere console) type `python3.` and then press the `Tab` key twice and
you should see something like the following:

    12:06 ~ $ python3.
    python3.10          python3.11-config   python3.13          python3.13t-config
    python3.10-config   python3.12          python3.13-config   python3.9
    python3.11          python3.12-config   python3.13t         python3.9m
    12:06 ~ $ python3.

If Python 3.13 is available, we will use it to create our virtual environment to support
Django 5.2 using the following Python command including the version number.

    cd ~
    python3.13 -m venv .ve52

If this works without error, you are in good shape.  If you get a message like

    python3.13: command not found

Try the `python` command above with 3.12, 3.11, and 3.10 until one works.   Hopefully your
account has at least one Python version that supports Django 5.2.

Once the above `venv` creation is successfull, activate your virtual environment and verify the python
version inside the virtual environment.

    source ~/.ve52/bin/activate
    python --version

Once you verify your Python version is correct, run:

    pip install --upgrade pip
    pip install django==5.2 ## this may take a couple of minutes

Sometimes these two commands take a long time.  Run them one at a time in the
shell.  When the servers are running slowly, each command can take more than ten
minutes to finish.  Be patient and wait until you see the `$` prompt indicating
the command is complete before continuing.  After they are complete, check your
Django version.

    python -m django --version

The Django version should be at least 5.2.


Checking out The Sample Code
----------------------------

Then checkout this repository:

    cd ~      # Or whatever folder
    source .ve52/bin/activate        # If needed

    git clone https://github.com/csev/dj4e-samples.git
    cd dj4e-samples
    git checkout django52

    pip install --upgrade pip
    pip install -r requirements52.txt
    python -m django --version

    python manage.py migrate
    python manage.py createsuperuser --username dj4e-samples
    # python manage.py changepassword dj4e-samples
    # dj4e_nn_!

    ...
    deactivate

Running Locally on Mac/Linux/WSL once the ve52 exists
-----------------------------------------------------

If you have Django installed on your local computer you can test any of the sample
applications by going into the folder and starting the server:

    cd dj4e-samples
    source .ve52/bin/activate   # If needed
    python manage.py runserver

And visit `http://localhost:8000`.

Running on PythonAnywhere (likely not needed)
---------------------------------------------

Yuo can always explore this code on https://samples.dj4e.com/ - so you don't really
need to run this on your own PythonAywhere.  But this is how Dr. Chuck sets it up on
his server in case he forgets :)

Once you have checked out the code under your home directory (`~`), and
ran the migrations and load scripts,
go under the Web tab, update the config files to point to your new application:

    Source code:                /home/--your-account--/dj4e-samples
    Working Directory:          /home/--your-account--/dj4e-samples

Use this as your `WGSI configuration file`:

    import os
    import sys

    path = os.path.expanduser('~/dj4e-samples')
    if path not in sys.path:
        sys.path.insert(0, path)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'dj4e-samples.settings'
    from django.core.wsgi import get_wsgi_application
    from django.contrib.staticfiles.handlers import StaticFilesHandler
    application = StaticFilesHandler(get_wsgi_application())

You can edit these files and settings in the Web tab to switch between
your various projects on PythonAnywhere.  Make sure to reload under the Web tab after
every file or configuration change.

Notes on new Django Versions
----------------------------

When you want to port this to a new Django version (likely once per year), create
a branch like `django62` and modify the following files:

* README.md

* home/templates/home/main.html

* tools/checkup.sh

Rename `requirements52.txt` to `requirments62.txt` and edit as needed.

