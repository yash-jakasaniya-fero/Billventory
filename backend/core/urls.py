from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SubscriptionViewSet, SupplierViewSet

router = DefaultRouter()
router.register(r'subscriptions', SubscriptionViewSet)
router.register(r'suppliers', SupplierViewSet)

urlpatterns = [
    path('', include(router.urls)),
]