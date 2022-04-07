from django.contrib import admin
from .models import State,Capital,Book,Author,Consumer,Distributors

# Register your models here.
class StateAdmin(admin.ModelAdmin):
    list_display = ['st_name']
admin.site.register(State,StateAdmin)

class CapitalAdmin(admin.ModelAdmin):
    list_display = ['cap_name','state']
admin.site.register(Capital,CapitalAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['bk_name']
admin.site.register(Book,BookAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ['auth_name','book']
admin.site.register(Author,AuthorAdmin)

class ConsumerAdmin(admin.ModelAdmin):
    list_display = ['cr_name']
admin.site.register(Consumer,ConsumerAdmin)

class DistributorsAdmin(admin.ModelAdmin):
    list_display = ['dist_name']
admin.site.register(Distributors,DistributorsAdmin)
