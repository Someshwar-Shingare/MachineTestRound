from django.contrib import admin
from .models import Laptop

# Register your models here.
class LaptopAdmin(admin.ModelAdmin):
    list_display = ['brand_name','model_name','ram','rom','ssd','processor','os','price']
admin.site.register(Laptop,LaptopAdmin)

