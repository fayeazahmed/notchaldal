from .models import Product
from django.contrib import admin


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category',
                    'price', 'in_stock', 'quantity')
    list_display_links = ('id', 'name', 'category',
                          'price')
    search_fields = ('id', 'name', 'category',
                     'price')


admin.site.register(Product, ProductAdmin)
