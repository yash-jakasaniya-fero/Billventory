from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Organization, OrganizationUser, OrganizationSubscription , OrganizationInventory, OrganizationProduct ,OrganizationBilling, OrganizationBillingItem, OrganizationPurchaseItem, OrganizationPurchaseOrder, OrganizationNotification
from .serializers import OrganizationCreateSerializer, OrganizationSerializer, OrganizationUserSerializer, OrganizationSubscriptionSerializer,OrganizationInventorySerializer, OrganizationProductSerializer, OrganizationBillingSerializer, OrganizationBillingItemSerializer, OrganizationPurchaseItemSerializer, OrganizationPurchaseOrderSerializer


class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationCreateSerializer

    @action(methods=['post'], detail=False)
    def create_organization(self, request, pk=None):
        organization_data = request.data.get('organization')
        user_data = request.data.get('user')
        subscription_data = request.data.get('subscription')

        serializer = OrganizationSerializer(data=organization_data)
        if serializer.is_valid():
            organization = serializer.save()

            user_serializer = OrganizationUserSerializer(data=user_data)
            if user_serializer.is_valid():
                user_serializer.save(organization=organization)

            subscription_serializer = OrganizationSubscriptionSerializer(data=subscription_data)
            if subscription_serializer.is_valid():
                subscription_serializer.save(organization=organization)

            return Response({
                'organization': serializer.data,
                'user': user_serializer.data,
                'subscription': subscription_serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        organizations = []

        for org in queryset:
            organization_data = OrganizationSerializer(org).data
            users_data = OrganizationUserSerializer(org.organization_users.all(), many=True).data
            subscriptions_data = OrganizationSubscriptionSerializer(org.organization_subscriptions.all(),many=True).data

            organizations.append({
                'organization': organization_data,
                'users': users_data,
                'subscriptions': subscriptions_data
            })

        return Response(organizations)


class OrganizationUserViewSet(viewsets.ModelViewSet):
    queryset = OrganizationUser.objects.all()
    serializer_class = OrganizationUserSerializer

class OrganizationSubscriptionsViewSet(viewsets.ModelViewSet):
    queryset = OrganizationSubscription.objects.all()
    serializer_class = OrganizationSubscriptionSerializer

    @action(methods=['post'],detail=False)
    def upgrade_subscriptions(self, request, pk=None):
        organization_subscription = self.get_object()
        new_plan = request.data.get('new_plan')

        if new_plan:
            organization_subscription.plan_name = new_plan
            organization_subscription.status = 'Active'
            organization_subscription.save()
            return Response(OrganizationSubscriptionSerializer(organization_subscription).data)

        return Response({'detail': 'New plan is required.'})

class OrganizationInventoryViewSet(viewsets.ModelViewSet):
    queryset = OrganizationInventory.objects.all()
    serializer_class = OrganizationInventorySerializer

    @action(methods=['post'],detail=False)
    def add_product(self, request, pk=None):
        inventory = self.get_object()
        product_name = request.data.get('product_name')
        product = OrganizationProduct.objects.create(organization=inventory.organization, product_name=inventory)
        return Response(
            {'message': 'Product added successfully', 'product': OrganizationProductSerializer(product).data})

    @action(methods=['post'],detail=False)
    def update_inventory(self, request, pk=None):
        inventory = self.get_object()
        inventory.quantity_in_stock = request.data.get('quantity_in_stock', inventory.quantity_in_stock)
        inventory.unit_price = request.data.get('unit_price', inventory.unit_price)
        inventory.save()
        return Response(OrganizationInventorySerializer(inventory).data)

class OrganizationProductViewSet(viewsets.ModelViewSet):
    queryset = OrganizationProduct.objects.all()
    serializer_class = OrganizationProductSerializer

class OrganizationBillingViewSet(viewsets.ModelViewSet):
    queryset = OrganizationBilling.objects.all()
    serializer_class = OrganizationBillingSerializer

    @action(methods=['post'],detail=False)
    def create_billing_item(self, request, pk=None):
        billing = self.get_object()
        serializer = OrganizationBillingItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            billing.total_items += 1
            billing.total_price += serializer.validated_data['line_item_price']
            billing.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    @action(methods=['post'],detail=False)
    def finalize_billing(self, request, pk=None):
        billing = self.get_object()
        billing.final_amount = billing.total_price + billing.total_tax - billing.discount
        billing.save()
        return Response(OrganizationBillingSerializer(billing).data)

class OrganizationBillingItemViewSet(viewsets.ModelViewSet):
    queryset = OrganizationBillingItem.objects.all()
    serializer_class = OrganizationBillingItemSerializer

class OrganizationPurchaseItemViewSet(viewsets.ModelViewSet):
    queryset = OrganizationPurchaseItem.objects.all()
    serializer_class = OrganizationPurchaseItemSerializer

    @action(methods=['post'],detail=False)
    def create_purchase_item(self, request, pk=None):
        total_price = request.data['purchase_price'] * request.data['quantity']
        purchase_item = OrganizationPurchaseItem.objects.create(
            organization_id=request.data['organization'],
            product_id=request.data['product'],
            quantity=request.data['quantity'],
            purchase_price=request.data['purchase_price'],
            total_price=total_price
        )
        return Response(OrganizationPurchaseItemSerializer(purchase_item).data)


class OrganizationPurchaseOrderViewSet(viewsets.ModelViewSet):
    queryset = OrganizationPurchaseOrder.objects.all()
    serializer_class = OrganizationPurchaseOrderSerializer

    @action(detail=True, methods=['post'])
    def create_purchase_order(self, request, pk=None):
        organization = self.get_object()
        purchase_items_data = request.data.get('purchase_items', [])
        total_amount_paid = sum(item['total_price'] for item in purchase_items_data)
        purchase_order = OrganizationPurchaseOrder.objects.create(
            organization=organization,
            supplier_id=request.data['supplier'],
            payment_method=request.data['payment_method'],
            total_amount_paid=total_amount_paid
        )
        purchase_order.purchase_items.set(purchase_items_data)
        for item in purchase_items_data:
            inventory_item = OrganizationInventory.objects.get(id=item['product'])
            inventory_item.quantity_in_stock += item['quantity']
            inventory_item.save()
        return Response(OrganizationPurchaseOrderSerializer(purchase_order).data)