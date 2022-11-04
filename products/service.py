from django.db.transaction import atomic

from products.models import Product, Attribute


class ProductService(object):
    def create_product(self, barcode_number=None, *args, **kwargs):
        """
        This method writen for create product
        :param barcode_number: Attribute name
        :param args:
        :param kwargs:
        attributes: {'key': 'value'}
        key type --> Attribute
        :return:
        """
        try:
            Product.objects.get(barcode=barcode_number)
            # TODO duplicated data handle for customer exception
        except Product.DoesNotExist:
            pass

        attributes = kwargs.pop("attributes")

        product = Product(**kwargs)

        product.set_attributes(**attributes)
        product.save()

        return product

    def update_product(self, instance, **kwargs):
        """
        Add only existing features
        :param instance:
        :param kwargs:
        :return:
        """
        attributes = kwargs.pop("attributes")
        instance.set_attributes(**attributes)
        instance.save()

    def delete_products(self, instance):
        """
        We do not want to delete the product completely. Because the product should be able to be active again.
        :param instance: Product
        :return:
        """
        instance.is_active = False
        instance.save()


class AttributeService(object):

    def create_attribute(self, name, **kwargs):
        pass

    def get_attribute(self, name):
        try:
            attribute = Attribute.objects.get(name=name)
            return attribute

        except Attribute.DoesNotExist:# TODO customer exception ex: Böyle bir attribute bulunamadı
            return

