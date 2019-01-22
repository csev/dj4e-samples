
from hashlib import sha256
from blobs.models import Blob, File
from django.db import models
from django.db.utils import IntegrityError

import sys

# https://docs.djangoproject.com/en/2.1/ref/files/uploads/#django.core.files.uploadedfile.UploadedFile

def handle_uploaded_file(f, application, applicationkey):
    max_size = 2 * 1024 * 2044;
    print('applicaton='+application+' key='+str(applicationkey))
    print('Size '+str(f.size));
    print('Name '+f.name);
    print('Content-type '+f.content_type);
    if ( f.size > max_size ) : return None

    bytearr = f.read();
    print(type(bytearr))
    print(len(bytearr))
    h1 = sha256()
    h1.update(bytearr)
    blob_sha256 = h1.hexdigest()
    print(blob_sha256)
    b = Blob(content=bytearr, sha256=blob_sha256)
    try:
        b.save()
        print('primary key='+str(b.id))
    except IntegrityError :
        try:
            b = Blob.objects.only('id').get(sha256=blob_sha256)
            print('primary key='+str(b.id))
        except Blob.DoesNotExist :
            print("Can't store, can't load - badly broken")
            return None

    # We have a blob, time to add the file entry

    f = File(sha256=blob_sha256, application=application, applicationkey=applicationkey,
            blob=b, contenttype=f.content_type, name=f.name)
    f.save()
    try : 
        print('file primary key='+str(f.id))
        return f
    except IntegrityError :
        print('file fail')


