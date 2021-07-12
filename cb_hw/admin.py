from django.contrib import admin

from .models import Author, Book, Comments, Publisher, Store


class BookInlineModelAdmin(admin.StackedInline):
    model = Book


@admin.register(Author)
class AuthorModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'age', 'id']


@admin.register(Comments)
class DiaryAdmin(admin.ModelAdmin):
    inlines = (BookInlineModelAdmin, )


@admin.register(Book)
class BookModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_authors', 'rating', 'pages', 'price', 'pubdate', 'publisher', 'id']


@admin.register(Store)
class StoreModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'display_books', 'id']


@admin.register(Publisher)
class PublisherModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'id']
