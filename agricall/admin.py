from django.contrib import admin

# Register your models here.
from .models import Products

@admin.register(Products) 
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'price','image', 'created_at', 'updated_at']