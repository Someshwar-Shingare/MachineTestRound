from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=10)
    city = models.CharField(max_length=10)
    standard = models.CharField(max_length=10)
    school = models.CharField(max_length=10)



class Employer(models.Model):
    Eid = models.IntegerField()
    Ename = models.CharField(max_length=10)
    Ecity = models.CharField(max_length=10)
    Emobno = models.IntegerField()
    Edesignation = models.CharField(max_length=10)
    Eaddress = models.CharField(max_length=10,default='abc')



class Animal(models.Model):

    Aname = models.CharField(max_length=10)
    Acolor = models.CharField(max_length=10)
    Alegs = models.IntegerField()
    Afoundin = models.CharField(max_length=10)
    Apet =  models.CharField(max_length=10)


class Laptop(models.Model):

    Lname = models.CharField(max_length=10)
    Lgeneration = models.CharField(max_length=10)
    Lram = models.CharField(max_length=10)
    Lhd = models.CharField(max_length=10)
    Lcolor = models.CharField(max_length=10)
    Lprice = models.CharField(max_length=10)


class Product(models.Model):
    Pid = models.IntegerField()
    Pname = models.CharField(max_length=10)
    Pmfg = models.CharField(max_length=10)
    Pexp = models.CharField(max_length=10)
    Pprice = models.CharField(max_length=10)