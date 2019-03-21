
from django import forms
from django.core.exceptions import ValidationError
from django.core import validators

class CommentForm(forms.Form):
    comment = forms.CharField(required=False, max_length=500, min_length=3, strip=True)
