from enumfields import EnumField
from enumfields.drf import EnumSupportSerializerMixin

from products.enums import ProductType
from products.models import Product, Attribute
from rest_framework import serializers
import json


# Serializers define the API representation.
class ProductSerializer(EnumSupportSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class AttributeSerializer(EnumSupportSerializerMixin, serializers.ModelSerializer):
    class Meta:
        model = Attribute
        fields = '__all__'


