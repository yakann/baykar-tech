from django.urls import path, include

from rest_framework import routers

# Routers provide an easy way of automatically determining the URL conf.
from products.api.views import ProductViewSet, AttributeViewSet
from users.api.views import BaykarCustomerViewSet

router = routers.DefaultRouter()
router.register(r'users', BaykarCustomerViewSet)
router.register(r'products', ProductViewSet)
router.register(r'attributes', AttributeViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]