from rest_framework import serializers
from .models import OrderedProduct
from orders.serializers import OrderSerializer
from products.serializers import ProductSerializer


class OrderedProductSerializer(serializers.ModelSerializer):
    order_source = OrderSerializer()
    product = ProductSerializer()

    class Meta:
        model = OrderedProduct
        fields = '__all__'
