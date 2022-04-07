from django.db import models

# Create your models here.

class Book(models.Model):
    id = models.IntegerField(primary_key=True)
    book_name = models.CharField(max_length=32)
    book_description = models.CharField(max_length=30)


class Author(models.Model):
    id = models.IntegerField(primary_key=True)
    auth_name = models.CharField(max_length=32)
    email = models.CharField(max_length=30)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, default='')


class Category(models.Model):
    id = models.IntegerField(primary_key=True)

    cat_name = models.CharField(max_length=32)




