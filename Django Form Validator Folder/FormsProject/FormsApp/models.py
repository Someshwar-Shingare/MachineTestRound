from django.db import models

# Create your models here.
class Student(models.Model):
    rn = models.IntegerField()
    name = models.CharField(max_length=32)
    marks = models.FloatField()

    def __str__(self):
        return f"{self.rn},{self.name},{self.marks}"



