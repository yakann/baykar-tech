import json

from rest_framework import viewsets, status
from rest_framework.response import Response

from products.models import Product, Attribute
from products.serializers import ProductSerializer, AttributeSerializer


# ViewSets define the view behavior.
from products.service import ProductService


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    product_service = ProductService()

    def perform_create(self, serializer):
        self.product_service.create_product(**serializer.data)

    def perform_update(self, serializer):
        validated_data = serializer.validated_data
        self.product_service.update_product(serializer.instance, **validated_data)

    def perform_destroy(self, instance):
        self.product_service.delete_products(instance)
"""
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(json.dumps(instance), status=status.HTTP_202_ACCEPTED)"""




class AttributeViewSet(viewsets.ModelViewSet):
    queryset = Attribute.objects.all()
    serializer_class = AttributeSerializer
