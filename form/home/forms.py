
from django import forms
from django.core.exceptions import ValidationError

class BasicForm(forms.Form):
    title = forms.CharField()
    mileage = forms.IntegerField()
    purchase_date = forms.DateField()

