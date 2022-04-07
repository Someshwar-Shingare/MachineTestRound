from django.contrib import admin
from .models import Student,Employer,Animal,Laptop,Product


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    List_display = ['rollno','name','city','standard','school']

admin.site.register(Student,StudentAdmin)


class EmployerAdmin(admin.ModelAdmin):
    List_display = ['Eid','Ename','Ecity','Emobno','Edesignation']

admin.site.register(Employer,EmployerAdmin)


class AnimalAdmin(admin.ModelAdmin):
    List_display = ['Aname','Acolor','Alegs','Afoundin','Apet']

admin.site.register(Animal,AnimalAdmin)


class LaptopAdmin(admin.ModelAdmin):
    List_display = ['Lname','Lgeneration','Lram','Lhd','Lcolor']

admin.site.register(Laptop,LaptopAdmin)


class ProductAdmin(admin.ModelAdmin):
    List_display = ['Pid','Pname','Pmfg','Pexp','Pprice']

admin.site.register(Product,ProductAdmin)
