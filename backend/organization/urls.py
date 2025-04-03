from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, OrganizationUserViewSet, OrganizationSubscriptionsViewSet, OrganizationInventoryViewSet, OrganizationProductViewSet, OrganizationBillingViewSet, OrganizationBillingItemViewSet, OrganizationPurchaseItemViewSet, OrganizationPurchaseOrderViewSet

router = DefaultRouter()
router.register('organization', OrganizationViewSet)
router.register('users', OrganizationUserViewSet)
router.register('subscriptions', OrganizationSubscriptionsViewSet)
router.register('inventory', OrganizationInventoryViewSet)
router.register('product', OrganizationProductViewSet)
router.register('sales-order', OrganizationBillingViewSet)
router.register('purchase-orders', OrganizationPurchaseOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
