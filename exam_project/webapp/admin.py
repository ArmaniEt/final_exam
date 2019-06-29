from django.contrib import admin
from webapp.models import Author, Book, UsersBookShelf


admin.site.register(Author)
admin.site.register(Book)
admin.site.register(UsersBookShelf)

