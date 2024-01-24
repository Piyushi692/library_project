from django.contrib import admin
from .models import Author, Book, Genre

# Register your models here.

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('user', 'phone', 'email', 'city', 'author_id')
    search_fields = ('user__username', 'email', 'city')

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'pages', 'author')
    list_filter = ('genre', 'author')
    search_fields = ('title', 'author__user__username')

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
