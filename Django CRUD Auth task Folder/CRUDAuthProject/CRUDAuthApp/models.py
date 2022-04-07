
from django.db import models

# Create your models here.
class Employer(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    mobno = models.IntegerField()
    designation = models.CharField(max_length=32)
    salary = models.FloatField()

