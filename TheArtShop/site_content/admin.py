from django.contrib import admin
from .models import Category, Product, Brand
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Определение ресурса для импорта/экспорта продуктов
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ('id', 'title_product', 'description_product', 'price_product', 'available', 'created', 'uploaded')

# Регистрация моделей в административном интерфейсе
admin.site.register(Brand)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title_category', 'slug_category']
    prepopulated_fields = {'slug_category': ('title_category',)}

@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    resource_class = ProductResource
    list_display = ['title_product', 'slug_product', 'price_product', 'available', 'created', 'uploaded']
    list_filter = ['available', 'created', 'uploaded']
    list_editable = ['price_product', 'available']
    prepopulated_fields = {'slug_product': ('title_product', )}

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Product)
