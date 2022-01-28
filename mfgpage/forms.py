from cProfile import label
from importlib.metadata import files
from pyexpat import model
from django.core import validators
from django import forms
from matplotlib import use
from .models import user , amenity
from django.db import models


class mfg_config(forms.ModelForm):
    class Meta:
        model =user
        fields=['Type','name','pic']
        labels={'pic':''}

class amenity(forms.ModelForm):
    class Meta:
        model=amenity
        fields=['name','uid']