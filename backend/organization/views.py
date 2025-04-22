from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from lib.views import BaseView

from .models import Organization, OrganizationUser, OrganizationSubscription, OrganizationInventory, \
    OrganizationProduct, OrganizationBilling, OrganizationBillingItem, OrganizationPurchaseItem, \
    OrganizationPurchaseOrder, OrganizationNotification, Supplier
from .serializers import OrganizationSerializer, OrganizationUserSerializer, OrganizationSubscriptionSerializer, \
    OrganizationInventorySerializer, OrganizationProductSerializer, OrganizationBillingSerializer, \
    OrganizationBillingItemSerializer, OrganizationPurchaseItemSerializer, OrganizationPurchaseOrderSerializer, \
    SupplierSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer

    def perform_create(self, serializer):
        serializer.save()

    @action(detail=False, methods=['get'])
    def list_organizations(self, request):
        organizations = Organization.objects.filter(user=request.user)
        serializer = self.get_serializer(organizations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class OrganizationUserViewSet(BaseView):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserSerializer

class OrganizationSubscriptionsViewSet(viewsets.ModelViewSet):
    queryset = OrganizationSubscription.objects.all()
    serializer_class = OrganizationSubscriptionSerializer

class SupplierViewSet(viewsets.ModelViewSet):
    queryset = Supplier.objects.all()
    serializer_class = SupplierSerializer


class OrganizationInventoryViewSet(BaseView):
    queryset = OrganizationInventory.objects.all()
    serializer_class = OrganizationInventorySerializer

class OrganizationProductViewSet(BaseView):
    queryset = OrganizationProduct.objects.all()
    serializer_class = OrganizationProductSerializer


class OrganizationBillingViewSet(viewsets.ModelViewSet):
    queryset = OrganizationBilling.objects.all()
    serializer_class = OrganizationBillingSerializer

    # def partial_update(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)
    #
    # @action(detail=False, methods=['patch'], url_path='update-by-rk-id/(?P<rk_id>[^/.]+)')
    # def update_by_rk_id(self, request, rk_id=None):
    #     try:
    #         billing = OrganizationBilling.objects.get(billing_id=rk_id)
    #     except OrganizationBilling.DoesNotExist:
    #         return Response({'detail': 'Billing not found'}, status=status.HTTP_404_NOT_FOUND)
    #
    #     serializer = self.get_serializer(billing, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)


class OrganizationPurchaseOrderViewSet(BaseView):
    queryset = OrganizationPurchaseOrder.objects.all()
    serializer_class = OrganizationPurchaseOrderSerializer

class OrganizationBillingItemViewSet(BaseView):
    queryset = OrganizationBillingItem.objects.all()
    serializer_class = OrganizationBillingItemSerializer

class OrganizationPurchaseItemViewSet(BaseView):
    queryset = OrganizationPurchaseItem.objects.all()
    serializer_class = OrganizationPurchaseItemSerializer