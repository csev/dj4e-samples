from django import forms
from meals.models import Meal
from django.core.files.uploadedfile import InMemoryUploadedFile

# https://docs.djangoproject.com/en/2.1/topics/http/file-uploads/
# https://stackoverflow.com/questions/2472422/django-file-upload-size-limit
# https://stackoverflow.com/questions/32007311/how-to-change-data-in-django-modelform
# https://docs.djangoproject.com/en/2.1/ref/forms/validation/#cleaning-and-validating-fields-that-depend-on-each-other

# Really simple naturalsize
def naturalsize(count) :
    fcount = float(count)
    k = 1024
    m = k * k
    g = m * k
    if fcount < k : return str(count) + 'B'
    if fcount >= k and fcount < m :
        return str(int(fcount / (k/10.0) ) / 10.0) + 'KB'
    if fcount >= m and fcount < g :
        return str(int(fcount / (m/10.0) ) / 10.0) + 'MB'
    return str(int(fcount / (g/10.0) ) / 10.0) + 'GB'

# Create the form class.
class CreateForm(forms.ModelForm):
    max_upload_limit = 2 * 1024 * 1024
    max_upload_limit_text = naturalsize(max_upload_limit)

    # Call this 'picture' so it gets copied from the form to the in-memory model
    # It will not be the "bytes", it will be the "InMemoryUploadedFile"
    # because we need to pull out things like content_type
    picture = forms.FileField(required=False, label='File to Upload <= '+max_upload_limit_text)
    upload_field_name = 'picture'

    class Meta:
        model = Meal
        fields = ['title', 'text', 'picture']  # Picture is manual

    def save(self, commit=True) :
        instance = super(CreateForm, self).save(commit=False)

        # We only need to process picture if it is a freshly uploaded file
        f = instance.picture   # Make a copy
        if isinstance(f, InMemoryUploadedFile):  # Extract data from the form to the model
            bytearr = f.read();
            # print('Received a file ',f.name,'size='+str(len(bytearr)),'type='+f.content_type)
            instance.content_type = f.content_type
            instance.picture = bytearr  # Overwrite with the actual image data

        if commit:
            instance.save()

        return instance

    def clean(self) :
        cleaned_data = super().clean()
        pic = cleaned_data.get('picture')
        if pic is None : return
        if len(pic) > self.max_upload_limit:
            self.add_error('picture', "File must be < "+self.max_upload_limit_text+" bytes")

