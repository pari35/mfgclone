from django.db import models

# Create your models here.
class Connector(models.Model):
    type=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    pic=models.ImageField(upload_to="static/images",default="")

class Amenity(models.Model):
    name=models.CharField(max_length=50)
    uid=models.IntegerField()
