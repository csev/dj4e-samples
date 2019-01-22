from django.http import HttpResponse
import logging

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

def upload_file(request):
    if request.method == 'POST':
        print('Title = '+request.POST['title'])
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})

def handle_uploaded_file(f):
    with open('/tmp/file.bin', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
