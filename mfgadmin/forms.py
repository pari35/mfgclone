from django import forms
from .models import Connector, Amenity
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class MfgConnector(forms.ModelForm):
    class Meta:
        model =Connector
        fields=['type','name','pic']
        labels={'pic':''}