from django.contrib import admin
from .models import Student,Employer,Laptop,Product,Animal

# Register your models here.
#admin.site.register(Student) it shows only object in admin panel

class StudentAdmin(admin.ModelAdmin):
    list_display = ['rollno','name','address']

admin.site.register(Student,StudentAdmin)

class EmployerAdmin(admin.ModelAdmin):
    list_display = ['eid','ename','ecity','emobno']

admin.site.register(Employer,EmployerAdmin)

class LaptopAdmin(admin.ModelAdmin):
    list_display = ['lname','lram','lhd','lprice']

admin.site.register(Laptop,LaptopAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['pname','pmfg','pexp','pprice']

admin.site.register(Product,ProductAdmin)

class AnimalAdmin(admin.ModelAdmin):
    list_display = ['name','color','legs']

admin.site.register(Animal,AnimalAdmin)
