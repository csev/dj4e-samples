from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class BasicForm(forms.Form):
    title = forms.CharField(validators=[
        validators.MinLengthValidator(2, "Please enter 2 or more characters")])
    mileage = forms.IntegerField()
    purchase_date = forms.DateField()

from django.forms import ModelForm
from form.models import Cat

# Create the form class.
class CatForm(ModelForm):
    class Meta:
        model = Cat
        # fields = ['name', 'breed', 'comments']
        fields = '__all__'


# References 

# https://docs.djangoproject.com/en/3.0/ref/forms/api/
# https://docs.djangoproject.com/en/3.0/ref/forms/fields/#datefield
# https://docs.djangoproject.com/en/3.0/ref/forms/validation/#using-validation-in-practice
# https://docs.djangoproject.com/en/3.0/ref/validators/
