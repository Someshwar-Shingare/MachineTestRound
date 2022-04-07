from django.contrib import admin
from .models import Employer

# Register your models here.

class EmployerAdmin(admin.ModelAdmin):
    list_display = ['name','email','mobno','designation','salary']

admin.site.register(Employer,EmployerAdmin)
