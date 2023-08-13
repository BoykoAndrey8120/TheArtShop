from django.contrib import admin
from .models import Category, Product, Brand



admin.site.register(Brand)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title_category', 'slug_category']
    prepopulated_fields = {'slug_category': ('title_category',)}

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title_product', 'slug_product', 'price_product', 'available', 'created', 'uploaded']
    list_filter = ['available', 'created', 'uploaded']
    list_editable = ['price_product', 'available']
    prepopulated_fields = {'slug_product': ('title_product', )}

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Product)
