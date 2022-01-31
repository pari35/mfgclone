from django.contrib import admin

from django.contrib import admin
from .models import Connector,Amenity


# Register your models here.
@admin.register(Connector)
class Connector(admin.ModelAdmin):
    list_display =('id','type','name','pic')


@admin.register(Amenity)
class Amenity(admin.ModelAdmin):
    list_display =('id','name')