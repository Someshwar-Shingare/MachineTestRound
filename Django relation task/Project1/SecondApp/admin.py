from django.contrib import admin
from .models import Person,UID,Department,Employees,User,Community

# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    list_display = ['pn_name']
admin.site.register(Person,PersonAdmin)

class UIDAdmin(admin.ModelAdmin):
    list_display = ['uid','person']
admin.site.register(UID,UIDAdmin)

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['dt_name']
admin.site.register(Department,DepartmentAdmin)

class EmployeesAdmin(admin.ModelAdmin):
    list_display = ['emp_name','department']
admin.site.register(Employees,EmployeesAdmin)

class UserAdmin(admin.ModelAdmin):
    list_display = ['user_name']
admin.site.register(User,UserAdmin)

class CommunityAdmin(admin.ModelAdmin):
    list_display = ['comm_name']
admin.site.register(Community,CommunityAdmin)
