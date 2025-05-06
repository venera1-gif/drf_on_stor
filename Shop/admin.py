from django.contrib import admin
from .models import  Category ,Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title','category', 'price','in_stock',)
    list_filter = ('category', 'in_stock')
    search_fields = ('title', 'description')