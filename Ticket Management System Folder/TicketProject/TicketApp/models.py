from django.db import models



# Create your models here.



class Ticket(models.Model):
    CATEGORY = (
        ('Travelling', 'Travelling'),
        ('Movie', 'Movie'),
        ('Tourism', 'Tourism')
    )
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for delivery', 'Out for delivery'),
        ('Delivered', 'Delivered'),
    )
    price = models.FloatField(null=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    description = models.CharField(max_length=200, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name







