from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=10)

class Employer(models.Model):
    eid = models.IntegerField()
    ename = models.CharField(max_length=10)
    ecity = models.CharField(max_length=10)
    emobno = models.IntegerField()

class Laptop(models.Model):
    lname = models.CharField(max_length=10)
    lram = models.CharField(max_length=10)
    lhd = models.CharField(max_length=10)
    lprice = models.IntegerField()

class Product(models.Model):
    pname = models.CharField(max_length=10)
    pmfg = models.IntegerField()
    pexp = models.IntegerField()
    pprice = models.IntegerField()


class Animal(models.Model):
    name = models.CharField(max_length=10)
    color = models.CharField(max_length=10)
    legs = models.IntegerField()


