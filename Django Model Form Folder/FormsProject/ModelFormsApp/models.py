from django.db import models

# Create your models here.
class Laptop(models.Model):
    company = models.CharField(max_length=32)
    model_name = models.CharField(max_length=32)
    ram = models.IntegerField(null=True)
    rom = models.IntegerField(null=True)
    price = models.FloatField(null=True)
