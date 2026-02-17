from django.db import models

# Create your models here.
class Client(models.Model):
    name = models.CharField(max_length=50)
    num = models.CharField(max_length=50)
    aadharno = models.CharField(max_length=50)
    CheckIn = models.CharField(max_length=50)
    CheckOut = models.CharField(max_length=50)
    city = models.CharField(max_length=50 , null=True)
    people = models.CharField(max_length=50, null=True)