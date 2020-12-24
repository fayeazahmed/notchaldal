from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product
from products.serializers import ProductSerializer
from .models import OrderedProduct
from .serializers import OrderedProductSerializer
# Create your views here.


class RetrieveOrderedProductsView(APIView):
    permission_classes = (permissions.IsAuthenticated, )

    def post(self, request, format=None):
        data = self.request.data
        id = data['id']

        products_ids = OrderedProduct.objects.filter(
            order_source__id=id).values_list('product_id', flat=True)
        products = Product.objects.filter(id__in=products_ids)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
