from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from .models import Product


class GetProductsView(APIView):
    permission_classes = (permissions.AllowAny, )

    def get(self, *args, **kwargs):
        category = kwargs['category']

        try:
            products = Product.objects.filter(category=category)
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)

        except:
            return Response(False)
