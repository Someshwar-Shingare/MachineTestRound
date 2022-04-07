from django.db import models

# Create your models here.
class Ticket(models.Model):
    user = models.ForeignKey(User)
    question = models.CharField(max_length=500, blank=False)
    admin_response = models.CharField(max_length=500, blank=True)
    accepted = models.BooleanField(default=False)

