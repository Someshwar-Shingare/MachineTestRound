
from django.contrib import admin
from .models import Book, Author, Category


# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ['id','book_name','book_description']
admin.site.register(Book, BookAdmin)




class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id','auth_name','email','book']
admin.site.register(Author, AuthorAdmin)






class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','cat_name']
admin.site.register(Category,CategoryAdmin)