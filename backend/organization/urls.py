from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OrganizationViewSet, OrganizationUserViewSet, OrganizationSubscriptionsViewSet, OrganizationInventoryViewSet, OrganizationProductViewSet, OrganizationBillingViewSet, OrganizationBillingItemViewSet, OrganizationPurchaseItemViewSet, OrganizationPurchaseOrderViewSet

router = DefaultRouter()
router.register(r'organizations', OrganizationViewSet)
router.register(r'organization-users', OrganizationUserViewSet)
router.register(r'organization-subscriptions', OrganizationSubscriptionsViewSet)
router.register(r'organization-inventories', OrganizationInventoryViewSet)
router.register(r'organization-products', OrganizationProductViewSet)
router.register(r'organization-billing-items', OrganizationBillingItemViewSet)
router.register(r'organization-billings', OrganizationBillingViewSet)
router.register(r'organization-purchase-items', OrganizationPurchaseItemViewSet)
router.register(r'organization-purchase-orders', OrganizationPurchaseOrderViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
