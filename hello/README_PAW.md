Running on PythonAnywhere
-------------------------

If you are using PythonAnywhere.com to run your DJango applications, you
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

Then `Reload` your application and then visit the site.

You should see the HTML in your browser, you will see the `logging.error()` output 
at the very end of your Error Log, and the output of the `print()` statement at 
the very end of your Server log.  These logs can be accessed from the Web tab in PYAW - 
make sure to scroll to the bottom of each log to see your messages.

If you are in the bash console, you can see the end of these logs using the following
command:

    tail /var/log/dj4e.pythonanywhere.com.server.log
    tail /var/log/dj4e.pythonanywhere.com.error.log

You can tell the `tail` command to attach itself to the end fo the log files and show
you anything that is appended to the log with the following commands:

Running DJango Locally
----------------------

If you have DJango running locally, it will look like this:

    $ python3 manage.py runserver
    Performing system checks...

    System check identified no issues (0 silenced).

    You have 14 unapplied migration(s). ...

    Starting development server at http://127.0.0.1:8000/
    Quit the server with CONTROL-C.
    ERROR:root:Hello world DJ4E in the log...
    Hello world DJ4E in a print statement...
    [22/Jan/2019 14:27:56] "GET / HTTP/1.1" 200 62

When you go to `http://127.0.0.1:8000/` in your browser you will see
the messages starting with "ERROR".

Don't worry about the migrations - we are not going to use sessions or administration
in this application.

The output from the `logging.error()` and the `print()` both come out on the console.
Of course the HTML is sent back to the browser.




