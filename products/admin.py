from django.contrib import admin
from .models import Category, Brand, Products

# Register your models here.


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    pass
