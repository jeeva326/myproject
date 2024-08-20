from django import forms
from .models import *

class DestinForm(forms.ModelForm):
    class Meta:
        model=Destin
        fields='__all__'