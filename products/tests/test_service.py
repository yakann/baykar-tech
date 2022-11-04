from unittest import TestCase
from model_mommy import mommy

from products.models import Product, Attribute
from products.enums import ProductType, AttributeType
from products.serializers import ProductSerializer
from products.service import ProductService


class ProductServiceTestCase(TestCase):
    """
    python manage.py test --keepdb products.tests.test_service.ProductServiceTestCase.test_create_product
    python manage.py test --keepdb products.test.ProductServiceTestCase.test_create_product

    """
    service = ProductService()

    def setUp(self):
        self.product = mommy.make(Product, name='IHA', barcode='2035432',
                                  is_active=True, product_type=ProductType.armor)

        self.attribute = mommy.make(Attribute, name='Sırt Destegi',
                                    attribute_type=AttributeType.seaman)

    def test_create_product(self):
        product1 = mommy.prepare(Product, name="iha", barcode="iha1",
                                 is_active=True, product_type=ProductType.armor)

        serializer = ProductSerializer(data=product1)
        product = self.service.create_product(serializer.data)

        self.assertEqual(product.attributes, {})

        attribute = {"Sırt Destegi": "Yumuşak doku"}
        product1["attributes"] = attribute

        serializer = ProductSerializer(product1)
        product = self.service.create_product(serializer.data)
        self.assertEqual(product.attributes, attribute)
