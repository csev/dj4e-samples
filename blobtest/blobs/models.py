from django.db import models

# Create your models here.

# Note to self...
# https://docs.djangoproject.com/en/2.1/ref/files/storage/
# https://stackoverflow.com/questions/54312624/is-there-an-implementation-of-a-single-instance-blob-store-for-django

class Blob(models.Model):
    sha256 = models.CharField(max_length=64, unique=True, help_text='The Checksum of the File.')
    deleted = models.BooleanField(default=False)
    content = models.BinaryField()
    # https://stackoverflow.com/questions/3429878/automatic-creation-date-for-django-model-form-objects
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class File(models.Model):
    name = models.CharField(max_length=256, help_text='The name of the file when first uploaded.')
    sha256 = models.CharField(max_length=64, help_text='The Checksum of the File.')
    blob = models.ForeignKey('Blob', on_delete=models.CASCADE)
    location = models.CharField(max_length=1024, help_text='The location of this file if it is not a blob')
    deleted = models.BooleanField(default=False)
    contenttype = models.CharField(max_length=256, help_text='The MIMEType of the file when first uploaded')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    accessed_at = models.DateTimeField(null=True)
    json = models.TextField()
    application = models.CharField(max_length=256, help_text='The application that created this file')
    applicationkey = models.IntegerField(help_text='A key within that application')

    # https://docs.djangoproject.com/en/2.1/ref/models/options/#unique-together
    # https://stackoverflow.com/questions/2201598/how-to-define-two-fields-unique-as-couple
    class Meta:
        unique_together = ('sha256', 'application', 'applicationkey')

    def __str__(self):
        """String for representing the Model object."""
        return self.name

