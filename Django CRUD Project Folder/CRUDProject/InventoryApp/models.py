from django.db import models

# Create your models here.
class Product(models.Model):
    category = models.CharField(max_length=32)
    company = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    qty = models.IntegerField()
    price = models.FloatField()

