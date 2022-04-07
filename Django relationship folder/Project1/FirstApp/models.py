from django.db import models


# Create your models here.
class Student(models.Model):
    rn = models.IntegerField()
    name = models.CharField(max_length=30)
    marks = models.FloatField()
    def __str__(self):
        return f"{self.rn},{self.name},{self.marks}"

class StudentData(models.Model):
    student = models.OneToOneField(Student,on_delete=models.CASCADE)
    city = models.CharField(max_length=32)
    pincode = models.CharField(max_length=30)

class Manufacturer(models.Model):
    comp_name = models.CharField(max_length=30)
    origin = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.comp_name},({self.origin})"



class Vehicle(models.Model):
    manufacturer = models.ForeignKey(Manufacturer,on_delete=models.CASCADE)
    veh_name = models.CharField(max_length=32)
    engine = models.CharField(max_length=30)
    price = models.FloatField()

class Course(models.Model):
    student = models.ManyToManyField(Student)
    cname = models.CharField(max_length=30)
    cfees = models.FloatField()




