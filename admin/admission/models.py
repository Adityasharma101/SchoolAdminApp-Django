
from django.db import models

# Create your models here.

class User(models.Model):
    sid=models.CharField(max_length=3 ,primary_key=True)
    name= models.CharField(max_length=30)
    Standard= models.CharField(max_length=30)
    age= models.CharField(max_length=3)
    city= models.CharField(max_length=30)

