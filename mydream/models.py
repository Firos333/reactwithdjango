import datetime 
from django.db import models
from django.contrib.auth.models import User
#from datetime import datetime, date

# Create your models here.

class Destinations1(models.Model):
    age = models.IntegerField()
    username=models.CharField(max_length=200)
    date_modified = models.DateTimeField(auto_now=True)
    is_draft = models.BooleanField() 

class Destinations2(models.Model):
    description = models.CharField(max_length=200)
    img = models.ImageField(upload_to ='pics')

    # object = models.Manager()

class Cards(models.Model):
    description = models.CharField(max_length=200)
    img = models.ImageField(upload_to ='pics')
    heading = models.CharField(max_length=200)
    # object = models.Manager()

class About(models.Model):
    story = models.CharField(max_length=800)
    img = models.ImageField(upload_to ='pics')
    title = models.CharField(max_length=200)

