from django.contrib import admin
from .models import Laptop

# Register your models here.

class LaptopAdmin(admin.ModelAdmin):
    list_display = ['company','name','ram','rom','price']

admin.site.register(Laptop,LaptopAdmin)
