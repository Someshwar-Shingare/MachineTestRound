from django.db import models

# Create your models here.
class Student(models.Model):
    rollno = models.IntegerField()
    name = models.CharField(max_length=10)
    marks = models.FloatField()


    def __str__(self):
        return f"{self.rollno},{self.name},{self.marks}"
