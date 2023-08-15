from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class BasicForm(forms.Form):
    title = forms.CharField(validators=[
        validators.MinLengthValidator(2, "Please enter 2 or more characters")
    ])
    mileage = forms.IntegerField()
    
    # add widget to date field for picking date easier 
    purchase_date = forms.DateField(
        widget=forms.TextInput(     
        attrs={'type': 'date'} 
    )
    )

# References 

# https://docs.djangoproject.com/en/4.2/ref/forms/api/
# https://docs.djangoproject.com/en/4.2/ref/forms/fields/#datefield
# https://docs.djangoproject.com/en/4.2/ref/forms/validation/#using-validation-in-practice
# https://docs.djangoproject.com/en/4.2/ref/validators/

