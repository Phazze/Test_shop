from django.contrib import admin
from .models import Products, Category


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'photo', 'time_create', 'author')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Products, ProductAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


admin.site.register(Category, CategoryAdmin)
