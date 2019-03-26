
# https://docs.djangoproject.com/en/2.1/topics/http/file-uploads/
from django import forms
from meals.models import Meal

# Create the form class.
class CreateForm(forms.ModelForm):
    file_data = forms.FileField(required=False)
    class Meta:
        model = Meal
        fields = ['title', 'text']  # Picture is manual

