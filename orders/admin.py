from .models import Order
from django.contrib import admin


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'date_ordered',
                    'preferred_time', 'total', 'delivered')
    list_display_links = ('id', 'customer', 'date_ordered',
                          'preferred_time', 'total',)
    search_fields = ('id', 'customer', 'date_ordered',
                     'preferred_time', 'total',)


admin.site.register(Order, OrderAdmin)
