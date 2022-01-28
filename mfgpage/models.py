from distutils.command.upload import upload
from tokenize import blank_re
from django.db import models
import uuid


# Create your models here.
class user(models.Model):
    Type=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    pic=models.ImageField(upload_to="static/images",default="")

class amenity(models.Model):
    name=models.CharField(max_length=50)
    uid=models.IntegerField()
