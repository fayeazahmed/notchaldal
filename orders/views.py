from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from .serializers import OrderSerializer
from .models import Order
from ordered_products.models import OrderedProduct
from products.models import Product
User = get_user_model()


class CreateOrderView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, format=None):
        data = self.request.data

        email = data['email']
        comments = data['comments']
        total = data['total']
        preferred_time = data['preferred_time']
        products = data['products']

        user = User.objects.get(email=email)
        order = Order.objects.create(
            customer=user, comments=comments, total=total, preferred_time=preferred_time)
        for product in products:
            id = product['id']
            quantity = product['quantity']
            product = Product.objects.get(id=id)
            OrderedProduct.objects.create(
                order_source=order, product=product, quantity=quantity)
        user.successful_orders += 1
        user.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)


class RetrieveOrderView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, format=None):
        data = self.request.data

        email = data['email']
        orders = Order.objects.filter(
            customer__email=email).order_by('id').reverse()
        serializer = OrderSerializer(orders, many=True)
        return Response(serializer.data)
