from django.contrib import admin

# Register your models here.
from .models import Category, Product


@admin.register(Category)
class CatAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class CatAdmin(admin.ModelAdmin):
    list_display = ['category', 'price', 'image', 'description',
                    'stock', 'price', 'update']
    list_filer = ['stock', 'price', 'category']
    prepopulated_fields = {'slug': ('title',)}
