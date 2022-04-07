from django.db import models

# Create your models here.
class Laptop(models.Model):
    brand_name = models.CharField(max_length=32)
    model_name = models.CharField(max_length=32)
    ram = models.IntegerField()
    rom = models.IntegerField()
    ssd = models.IntegerField()
    processor = models.CharField(max_length=30)
    os = models.CharField(max_length=32)
    price = models.FloatField(max_length=32)

