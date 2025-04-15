from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, OrganizationUserViewSet, OrganizationSubscriptionsViewSet, OrganizationInventoryViewSet, OrganizationProductViewSet, OrganizationBillingViewSet,OrganizationPurchaseItemViewSet,OrganizationBillingItemViewSet, OrganizationPurchaseOrderViewSet, SupplierViewSet

router = DefaultRouter()
router.register('organization', OrganizationViewSet)
router.register('users', OrganizationUserViewSet)
router.register('subscriptions', OrganizationSubscriptionsViewSet)
router.register('supplier',SupplierViewSet)
router.register('inventory', OrganizationInventoryViewSet)
router.register('product', OrganizationProductViewSet)
router.register('sales-order', OrganizationBillingViewSet)
router.register('sales-items', OrganizationBillingItemViewSet)
router.register('purchase-orders', OrganizationPurchaseOrderViewSet)
router.register('purchase-items', OrganizationPurchaseItemViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
