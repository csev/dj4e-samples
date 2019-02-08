DJ4E Samples
============

This is a set of Django projects that provide free sample code to
support the www.dj4e.com web site.

To set this up, simply check it out into some folder

    cd ...wherever...
    git clone https://github.com/csev/dj4e-samples.git

Each of the subfolders below dj4e-samples is a Django project that
contains zero or more applications.  

These samples may be updated from time to tims so you might want to get updates
using `git pull`.  Also if there are bugs, you are welcome to submit
a Pull Request on github.

All of the documentation material is copyright CC-BY 3.0 and the Code is copyright MIT
by whomever wrote the code or documentation.  You are welcome to use this in any way you see
fit and paste code from this repo into your applications.

Running Locally
---------------

If you have Django installed on your local computer you can test any of the sample
applications bygoing into the folder and starting the server:

    cd dj4e-samples
    cd hello
    python3 manage.py runserver

And visit `http://localhost:8000`.

When running locally you just wander around the projects and do a `runserver` in
any of the project folders to test any of the projects.

Running on PythonAnywhere
-------------------------

If you are using PythonAnywhere.com to run your Django applications, you
can check all the sample code out as follows:

    cd ~
    git clone https://github.com/csev/dj4e-samples.git

Then under the web tab, update the config files to point to your new application:

    Source code:                /home/--your-account--/dj4e-samples/hello
    Working Directory:          /home/--your-account--/dj4e-samples/hello

Update the lines in your `WGSI configuration file`:

    ...
    path = os.path.expanduser('~/dj4e-samples/hello')
    ...
    os.environ['DJANGO_SETTINGS_MODULE'] = 'hello.settings'

Then `Reload` your application and then visit the site.   If the top level folder
insists on redirecting to `/catalog` simply clear your cache.

You can edit these files and settings in the Web tab to easily switch between
the various projects in this repository.

Approximate Order
-----------------

    hello - Project layout
    getpost - HTTP get / post

    users - One table model / SQL  / django shell
    tracks - Many to one models / SQL / django shell

    views - Function and class views
    tmpl - Templates examples

    generic - Looking at generic views - cats/dogs/horses/autos
    session 

    form - Using forms.py
    autoscrud 

