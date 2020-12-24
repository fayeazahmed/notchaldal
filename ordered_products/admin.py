from .models import OrderedProduct
from django.contrib import admin


class OrderedProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'order_source', 'product',
                    'quantity')
    list_display_links = ('id', 'order_source', 'product',
                          'quantity')
    search_fields = ('id', 'order_source', 'product',
                     'quantity')


admin.site.register(OrderedProduct, OrderedProductAdmin)
