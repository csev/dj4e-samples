from django.forms import ModelForm
from autos.models import Make


# Create the form class.
class MakeForm(ModelForm):
    class Meta:
        model = Make
        fields = '__all__'
