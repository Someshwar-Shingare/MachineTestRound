from django.contrib import admin
from .models import Appointment, Ambulance, Doctor, NursingStaff, RoomServiceStaff, Category, Product, CustomerOrder, Customer

# Register your models here.
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ['name','gender','city','previous_visit','if_before_visited_visit_detail', 'appointment_date', 'slot', 'contact_number']
admin.site.register(Appointment,AppointmentAdmin)

class AmbulanceAdmin(admin.ModelAdmin):
    list_display = ['patient_name', 'patient_age', 'gender', 'contact_number', 'location', 'disease']
admin.site.register(Ambulance,AmbulanceAdmin)

class DoctorAdmin(admin.ModelAdmin):
    list_display = ['name','gender','address','age','qualification', 'aadhaar_number']
admin.site.register(Doctor, DoctorAdmin)

class NursingStaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'address', 'age', 'qualification', 'aadhaar_number']
admin.site.register(NursingStaff, NursingStaffAdmin)

class RoomServiceStaffAdmin(admin.ModelAdmin):
    list_display = ['name', 'gender', 'address', 'age', 'aadhaar_number']
admin.site.register(RoomServiceStaff, RoomServiceStaffAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']
admin.site.register(Category, CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'price', 'description', 'image']
admin.site.register(Product, ProductAdmin)




admin.site.register(Customer)


@admin.register(CustomerOrder)
class CustomerOrderAdmin(admin.ModelAdmin):
    list_display = ['order_no', 'product_name', 'unit_price', 'quantity', 'total_price']
    list_filter = ('customer__name',)

    def product_name(self, obj):
        return obj.product.name

    def order_no(self, obj):
        return f'#{obj.id}'

    def unit_price(self, obj):
        return obj.product.price

    def total_price(self, obj):
        return obj.product.price * obj.quantity



