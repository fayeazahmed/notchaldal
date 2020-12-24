from rest_framework import serializers
from .models import Order
from users.serializers import UserSerializer


class OrderSerializer(serializers.ModelSerializer):
    customer = UserSerializer()

    class Meta:
        model = Order
        fields = '__all__'
