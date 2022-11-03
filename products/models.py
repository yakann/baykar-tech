from django.db import models

from enumfields import EnumField

from products.enums import AttributeType, ProductType
from utils.models import StarterModel


class Product(StarterModel, models.Model):
    name = models.CharField(max_length=55)
    barcode = models.CharField(max_length=16)
    title = models.CharField(max_length=65)
    description = models.CharField(max_length=165)
    type = EnumField(ProductType, null=True, blank=True)
    attributes = models.JSONField(null=True, default={})
    is_active = models.BooleanField()

    # TODO language_field for different language

    def __str__(self):
        return self.name

    def set_attributes(self, attribute_name=None, value=None, **kwargs):
        """
        İnput multiple values and set attributes
        :param attribute_name: Attribute Name
        :param value: any type value
        :param kwargs: {"name": attribute_value}
        :return:
        """
        # TODO language version
        attributes = {}
        if kwargs:
            for name, value in kwargs.items():
                if self.exist_attribute(name):
                    attributes[name] = value
        else:
            attributes = {attribute_name: value}
        # TODO error report: error service for logging because attribute not create
        self.attributes.update(attributes)

    def exist_attribute(self, name):
        return Attribute.objects.filter(name=name).exists()


class Attribute(StarterModel, models.Model):
    name = models.CharField(max_length=35)
    type = EnumField(AttributeType, null=True, blank=True)

    def __str__(self):
        return self.name
