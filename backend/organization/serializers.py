from datetime import timezone
from itertools import product
import uuid
from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Organization, OrganizationUser, OrganizationSubscription, OrganizationInventory, \
    OrganizationProduct, OrganizationBilling, OrganizationBillingItem, OrganizationPurchaseItem, \
    OrganizationPurchaseOrder, Supplier


class OrganizationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationUser
        fields = ['org_user', 'user_email', 'user_role', 'is_active']

class OrganizationSerializer(serializers.ModelSerializer):
    organization_users = OrganizationUserSerializer

    class Meta:
        model = Organization
        fields = ['user','org_id', 'org_name', 'org_address', 'org_logo', 'has_gst_number', 'gst_number']

    def validate(self, attrs):
        user = attrs.get('user')
        if Organization.objects.filter(user=user).exists():
            raise serializers.ValidationError("This user already has an organization.")
        return attrs


class OrganizationSubscriptionSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrganizationSubscription
        fields = ['organization', 'plan_name', 'plan_price', 'start_date', 'end_date', 'status']

    def validate(self, attrs):
        organization = attrs.get('organization')
        if self.instance:
            return attrs
        active_subs = OrganizationSubscription.objects.filter(
            organization=organization,
        )
        if active_subs.exists():
            raise serializers.ValidationError("An active subscription already exists for this organization.")
        return attrs



class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['supplier_code','email','gst_number','name','contact_person','address']

    def create(self, validated_data):
        if not validated_data.get('supplier_code'):
            validated_data['supplier_code'] = self.generate_supplier_code()
        return super().create(validated_data)

    def update(self, instance, validated_data):
        validated_data.pop('supplier_code', None)
        return super().update(instance, validated_data)

    def generate_supplier_code(self):
        return f"SUP-{uuid.uuid4().hex[:6].upper()}"


class OrganizationInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationInventory
        fields = ['organization', 'product_name',  'unit_price', 'quantity_in_stock']

class OrganizationProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = OrganizationProduct
        fields = ['id', 'product_name']


class OrganizationBillingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationBillingItem
        fields = ['product_name', 'product_quantity', 'unit_price', 'line_item_price']

class OrganizationBillingSerializer(serializers.ModelSerializer):
    billing_items = OrganizationBillingItemSerializer(many=True)

    class Meta:
        model = OrganizationBilling
        fields = ['id','organization', 'billing_id', 'payment_method', 'total_quantities', 'total_items', 'total_price',
                  'total_tax', 'discount', 'tax_percentage', 'final_amount', 'gst_number', 'billing_items']

    def create(self, validated_data):
        billing_items_data = validated_data.pop('billing_items')
        validated_data['billing_id'] = f"BILL-{uuid.uuid4().hex[:8].upper()}"
        total_quantities = 0
        total_items = 0
        total_price = 0
        billing = OrganizationBilling.objects.create(**validated_data)
        organization = validated_data['organization']
        for item_data in billing_items_data:
            product_name = item_data['product_name']
            quantity = item_data['product_quantity']
            unit_price = item_data['unit_price']
            line_item_price = quantity * unit_price
            item_data['line_item_price'] = line_item_price
            total_quantities += quantity
            total_items += 1
            total_price += line_item_price
            try:
                inventory = OrganizationInventory.objects.get(organization=organization, product_name=product_name)
            except OrganizationInventory.DoesNotExist:
                raise serializers.ValidationError(f"{product_name} not available in inventory")
            if inventory.quantity_in_stock < quantity:
                raise serializers.ValidationError(f"Insufficient stock for {product_name}")
            inventory.quantity_in_stock -= quantity
            inventory.save()
            OrganizationBillingItem.objects.create(billing=billing, **item_data)
        tax_percentage = 18
        total_tax = total_price * tax_percentage / 100
        discount = 200 if total_price > 2000 else 0
        final_amount = total_price + total_tax - discount
        billing.total_quantities = total_quantities
        billing.total_items = total_items
        billing.total_price = total_price
        billing.total_tax = total_tax
        billing.tax_percentage = tax_percentage
        billing.discount = discount
        billing.final_amount = final_amount
        billing.save()
        return billing


    # def update(self, instance, validated_data):
    #     billing_items_data = validated_data.pop('billing_items')
    #     instance.billing_items.all().delete()
    #     organization = validated_data.get('organization', instance.organization)
    #     for item_data in billing_items_data:
    #         product_name = item_data['product_name']
    #         quantity = item_data['product_quantity']
    #         try:
    #             inventory = OrganizationInventory.objects.get(organization=organization, product_name=product_name)
    #         except OrganizationInventory.DoesNotExist:
    #             raise serializers.ValidationError(f"{product_name} not available in inventory")
    #         if inventory.quantity_in_stock < quantity:
    #             raise serializers.ValidationError(f"Insufficient stock for {product_name}")
    #         inventory.quantity_in_stock -= quantity
    #         inventory.save()
    #         OrganizationBillingItem.objects.create(billing=instance, **item_data)
    #     return super().update(instance, validated_data)

class OrganizationPurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationPurchaseItem
        fields = ['product_name', 'product_quantity', 'unit_price', 'line_item_price']

class OrganizationPurchaseOrderSerializer(serializers.ModelSerializer):
    purchase_items = OrganizationPurchaseItemSerializer(many=True)

    class Meta:
        model = OrganizationPurchaseOrder
        fields = ['organization','id','supplier', 'purchase_date', 'payment_method', 'total_amount_paid', 'purchase_items']
        read_only_fields = ['id']

    def create(self, validated_data):
        total_price = 0
        purchase_items_data = validated_data.pop('purchase_items')
        purchase_order = OrganizationPurchaseOrder.objects.create(**validated_data)
        organization = validated_data['organization']
        for item_data in purchase_items_data:
            product_name = item_data['product_name']
            quantity = item_data['product_quantity']
            unit_price = item_data['unit_price']
            line_item_price = quantity * unit_price
            item_data['line_item_price'] = line_item_price
            total_price += line_item_price
            try:
                inventory = OrganizationInventory.objects.get(organization=organization, product_name=product_name)
                inventory.quantity_in_stock += quantity
                inventory.unit_price = unit_price
                inventory.save()
            except OrganizationInventory.DoesNotExist:
                OrganizationInventory.objects.create(
                    organization=organization,
                    product_name=product_name,
                    product_quantity=quantity,
                    quantity_in_stock=quantity,
                    unit_price=unit_price
                )
            OrganizationPurchaseItem.objects.create(purchase_order=purchase_order, **item_data)
        purchase_order.total_amount_paid = total_price
        return purchase_order

    # def update(self, instance, validated_data):
    #     purchase_items_data = validated_data.pop('purchase_items')
    #     instance.purchase_items.all().delete()
    #     organization = validated_data.get('organization', instance.organization)
    #     for item_data in purchase_items_data:
    #         product_name = item_data['product_name']
    #         quantity = item_data['product_quantity']
    #         unit_price = item_data['unit_price']
    #         try:
    #             inventory = OrganizationInventory.objects.get(organization=organization, product_name=product_name)
    #             inventory.quantity_in_stock += quantity
    #             inventory.unit_price = unit_price
    #             inventory.save()
    #         except OrganizationInventory.DoesNotExist:
    #             OrganizationInventory.objects.create(
    #                 organization=organization,
    #                 product_name=product_name,
    #                 product_quantity=quantity,
    #                 quantity_in_stock=quantity,
    #                 unit_price=unit_price
    #             )
    #         OrganizationPurchaseItem.objects.create(purchase_order=instance, **item_data)
    #     return super().update(instance, validated_data)
