from django.db import models

# Create your models here.
class Employee(models.Model):
    eno = models.IntegerField()
    ename = models.CharField(max_length=32)
    emob = models.IntegerField()
    edesignation = models.CharField(max_length=32)
    esal = models.FloatField()
    ecity = models.CharField(max_length=32)
    image = models.ImageField(upload_to='myimage')
    date_created = models.DateTimeField(auto_now_add=True)

