import imp
from django.contrib import admin
from django.forms import models
from .models import user

# Register your models here.
@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display =('id','Type','name')