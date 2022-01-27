from django.db import models

# Create your models here.
class user(models.Model):
    Type=models.CharField(max_length=50)
    name=models.CharField(max_length=50)
    