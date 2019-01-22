
# https://docs.djangoproject.com/en/2.1/topics/http/file-uploads/
from django import forms

class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()

