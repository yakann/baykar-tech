from rest_framework import viewsets
from users.models import BaykarCustomer
from users.serializers import BaykarCustomerSerializer


# ViewSets define the view behavior.
class BaykarCustomerViewSet(viewsets.ModelViewSet):
    queryset = BaykarCustomer.objects.all()
    serializer_class = BaykarCustomerSerializer