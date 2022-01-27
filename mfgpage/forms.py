from django.core import validators
from django import forms
from matplotlib import use
from .models import user
from django.db import models


class mfg_config(forms.ModelForm):
    class Meta:
        model =user
        fields=["Type",'name']