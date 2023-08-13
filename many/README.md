
Many to Many Relationships and Script Loading of Data
-----------------------------------------------------

This folder and the `scripts` folder are part of the data loading
exercise.

This folder contains the data model in `models.py` and the `scripts`
folder contains the loading script `many_load.py`.

The Python code in the script is not just Python.  It needs to load up
all of Django so the code can access the data models and database.
Python has an extension that makes it easier to run scripts after fully
loadinfd Django as long as the extensions (see requirements.txt) are loaded.

Run the following command from the folder above this one (with manage.py):

    python3 manage.py runscript many_load

References
----------

https://django-extensions.readthedocs.io/en/latest/runscript.html

https://docs.djangoproject.com/en/4.2/topics/db/models/#extra-fields-on-many-to-many-relationships

https://docs.djangoproject.com/en/4.2/ref/models/fields/#choices

