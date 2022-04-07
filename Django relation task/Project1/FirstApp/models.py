from django.db import models

# Create your models here.
class State(models.Model):

    st_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.st_name}"


class Capital(models.Model):
    state = models.OneToOneField(State,on_delete=models.CASCADE)
    cap_name = models.CharField(max_length=30)


class Book(models.Model):

    bk_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.bk_name}"


class Author(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    auth_name = models.CharField(max_length=30)


class Consumer(models.Model):

    cr_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.cr_name}"


class Distributors(models.Model):
    consumer = models.ManyToManyField(Consumer)
    dist_name = models.CharField(max_length=30)
