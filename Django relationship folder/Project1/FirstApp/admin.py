from django.contrib import admin
from .models import Student,StudentData,Manufacturer,Vehicle,Course


# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ['rn','name','marks']
admin.site.register(Student,StudentAdmin)

class StudentDataAdmin(admin.ModelAdmin):
    list_display = ['city','pincode','student']
admin.site.register(StudentData,StudentDataAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['comp_name','origin']
admin.site.register(Manufacturer,ManufacturerAdmin)

class VehicleAdmin(admin.ModelAdmin):
    list_display = ['veh_name','engine','price','manufacturer']
admin.site.register(Vehicle,VehicleAdmin)

class CourseAdmin(admin.ModelAdmin):
    list_display = ['cname','cfees']
admin.site.register(Course,CourseAdmin)



