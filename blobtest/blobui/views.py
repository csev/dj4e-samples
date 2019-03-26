from django.http import HttpResponse, StreamingHttpResponse
import logging

from blobs.models import File, Blob

import blobs.utils

logger = logging.getLogger(__name__)

# Create your views here.

def index(request):
    response = """<html><body><p>BLOB Test DJ4E in HTML</p>
    <p>This sample code is available at
    <a href="https://github.com/csev/dj4e-samples">
    https://github.com/csev/dj4e-samples</a></p>
    <p><a href="upload">Upload form</a></p>
    </body></html>"""
    return HttpResponse(response)

def success(request):
    response = """<html><body><p>Success</p>
    <p><a href="..">Start over</a></p>
    </body></html>"""
    return HttpResponse(response)

from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm

# Imaginary function to handle an uploaded file.
# from somewhere import handle_uploaded_file

from random import *

def upload_file(request):
    if request.method == 'POST':
        print('Title = '+request.POST['title'])
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            appkey = int(random() * 999999)
            blobs.utils.handle_uploaded_file(request.FILES['file'], 'testing', appkey)
            return HttpResponseRedirect('/success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})


# https://djangobook.com/request-response-objects/

from django.shortcuts import get_object_or_404
def stream_file(request, pk) :
    blob = get_object_or_404(Blob, id=pk)
    fdata = get_object_or_404(File, sha256=blob.sha256)
    response = HttpResponse()
    response['Content-Type'] = fdata.contenttype
    response['Content-Length'] = len(blob.content)
    response.write(blob.content)
    return response

# Streaming notes...

# https://github.com/edilio/StreamingHttpResponse/blob/master/StreamingHttpResponse/apps/stream/views.py
# https://docs.djangoproject.com/en/2.1/ref/request-response/#streaminghttpresponse-objects
# https://www.programcreek.com/python/example/52439/django.http.StreamingHttpResponse
