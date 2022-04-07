from django.contrib import admin
from .models import Employee

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['eno', 'ename', 'emob', 'edesignation', 'esal', 'ecity','image','date_created']
admin.site.register(Employee,EmployeeAdmin)

