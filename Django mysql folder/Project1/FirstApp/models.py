from django.db import models


# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=10)
    marks = models.FloatField()
    address = models.CharField(max_length=20,default='abc')
    city = models.CharField(max_length=20,null=True)
