from django.contrib import admin
from .models import Book,Author
# Register your models here.

class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "count_in_library")
    
admin.site.register(Author)
admin.site.register(Book,BookAdmin)