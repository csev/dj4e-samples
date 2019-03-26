
# https://docs.djangoproject.com/en/2.1/topics/http/file-uploads/
from django import forms
from meals.models import Meal

# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://docs.djangoproject.com/en/2.1/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other

# Create the form class.
class CreateForm(forms.ModelForm):
    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    picture = forms.FileField(required=False)
    max_upload_limit = 1 * 1024 * 1024

    class Meta:
        model = Meal
        fields = ['title', 'text', 'picture']  # Picture is manual

    def clean(self) :
        cleaned_data = super().clean()
        size = len(cleaned_data.get('picture'))
        if size > self.max_upload_limit:
            self.add_error('picture', "File must be < "+str(self.max_upload_limit)+" bytes")

