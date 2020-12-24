from django.db import models
from orders.models import Order
from products.models import Product

# Create your models here.


class OrderedProduct(models.Model):
    order_source = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return "ID: " + str(self.order_source_id) + " Customer: " + str(self.order_source)
