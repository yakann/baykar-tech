from users.models import BaykarCustomer
from rest_framework import routers, serializers


# Serializers define the API representation.
class BaykarCustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BaykarCustomer
        fields = ['url', 'username', 'email', 'is_staff']