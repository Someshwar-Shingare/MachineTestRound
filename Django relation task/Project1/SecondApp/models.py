from django.db import models

# Create your models here.
class Person(models.Model):

    pn_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.pn_name}"


class UID(models.Model):
    person = models.OneToOneField(Person,on_delete=models.CASCADE)
    uid = models.IntegerField()


class Department(models.Model):

    dt_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.dt_name}"


class Employees(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    emp_name = models.CharField(max_length=30)


class User(models.Model):

    user_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.user_name}"


class Community(models.Model):
    user = models.ManyToManyField(User)
    comm_name = models.CharField(max_length=30)

