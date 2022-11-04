from unittest import TestCase
from model_mommy import mommy

from products.models import Product, Attribute
from products.enums import ProductType, AttributeType
from products.serializers import ProductSerializer
from products.service import ProductService


class ProductServiceTestCase(TestCase):
    """
    python manage.py test --keepdb products.tests.test_service.ProductServiceTestCase.test_create_product

    """
    service = ProductService()

    def setUp(self):
        self.product = mommy.make(Product, name='IHA',
            barcode='2035432', is_active=True)

        self.attribute = mommy.make(Attribute, name='Sırt Destegi',
            attribute_type=AttributeType.seaman)

    def test_create_product(self):
        product1 = mommy.prepare(Product, name="iha", barcode="iha1",
            is_active=True)

        serializer = ProductSerializer(data=product1)
        self.assertTrue(serializer.is_valid(raise_exception=True))
        product = self.service.create_product()

        self.assertEqual(product.attributes, {})

        product1["attributes"] = {"Sırt Destegi": "Yumuşak doku"}

        serializer = ProductSerializer(data=product1)
        self.assertTrue(serializer.is_valid(raise_exception=True))
        self.service.create_product()
