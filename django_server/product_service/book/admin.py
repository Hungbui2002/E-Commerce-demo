from django.contrib import admin

# Register your models here.
# Register your models here.
from book.models import Author, Publisher, Book

admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)