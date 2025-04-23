from datetime import timezone
from itertools import product
import uuid
from rest_framework import serializers, status
from rest_framework.response import Response

from .models import Organization, OrganizationUser, OrganizationSubscription, OrganizationInventory, \
    OrganizationProduct, OrganizationBilling, OrganizationBillingItem, OrganizationPurchaseItem, \
    OrganizationPurchaseOrder, Supplier, OrganizationOnBoarding


class EmailOTPSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationOnBoarding
        fields = ['email']
        extra_kwargs = {
            'email': {'validators': []}
        }

    def validate_email(self, attrs):
        instance = OrganizationOnBoarding.objects.filter(email=attrs).first()
        if instance and instance.is_verified:
            raise serializers.ValidationError("This email is already verified.")
        return attrs

class EmailOTPVerificationSerializer(serializers.Serializer):
    email = serializers.EmailField()
    otp = serializers.CharField(max_length=6)

    def validate(self, attrs):
        email = attrs['email']
        otp = attrs.get('otp')

        try:
            instance = OrganizationOnBoarding.objects.get(email=email)
        except OrganizationOnBoarding.DoesNotExist:
            raise serializers.ValidationError("OTP was not requested for this email.")

        if instance.is_verified:
            raise serializers.ValidationError("This email has already been verified.")

        if instance.otp != otp:
            raise serializers.ValidationError("The OTP you entered is invalid.")

        return attrs

    def create(self, validated_data):
        otp_obj = validated_data['otp_obj']
        otp_obj.is_verified = True
        otp_obj.save()
        return otp_obj

class OrganizationOnBoardingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationOnBoarding
        fields = '__all__'

    def validate_email(self, value):
        try:
            instance = OrganizationOnBoarding.objects.get(email=value)
        except OrganizationOnBoarding.DoesNotExist:
            raise serializers.ValidationError("You must verify your email before completing onboarding.")

        if not instance.is_verified:
            raise serializers.ValidationError("Email is not verified.")
        return value

    def create(self, validated_data):
        email = validated_data['email']
        OrganizationOnBoarding.objects.filter(email=email).update(is_verified=True)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

class OrganizationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationUser
        fields = ['id','org_user', 'user_email', 'user_role', 'is_active']


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['org_id', 'user', 'org_name', 'org_address', 'org_logo', 'has_gst_number', 'gst_number']

    def validate_user(self, value):
        if Organization.objects.filter(user=value).exists():
            raise serializers.ValidationError("This user already has an organization.")
        return value

    def create(self, validated_data):
        return Organization.objects.create(**validated_data)


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
        fields = ['id','supplier_code','email','gst_number','name','contact_person','address']

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
        fields = ['id', 'organization', 'product_name', 'unit_price', 'quantity_in_stock']

    def validate_unit_price(self, value):
        if value is None or value <= 0:
            raise serializers.ValidationError("Unit price must be greater than 0.")
        return value

    def validate_quantity_in_stock(self, value):
        if value is None or value <= 0:
            raise serializers.ValidationError("Product quantity must be greater than 0.")
        return value

    def create(self, validated_data):
        organization = validated_data.get('organization')
        product_name = validated_data.get('product_name')
        unit_price = validated_data.get('unit_price')
        quantity = validated_data.get('quantity_in_stock')

        existing_item = OrganizationInventory.objects.filter(
            organization=organization,
            product_name=product_name
        ).first()

        if existing_item:
            existing_item.quantity_in_stock += quantity
            existing_item.unit_price = unit_price
            existing_item.save()
            return existing_item
        else:
            return super().create(validated_data)

class OrganizationProductSerializer(serializers.ModelSerializer):

    class Meta:

        model = OrganizationProduct
        fields = ['id', 'product_name']


class OrganizationBillingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationBillingItem
        fields = ['product_name', 'product_quantity', 'unit_price', 'line_item_price']

    def validate_product_quantity(self, value):
        if value is None or value <= 0:
            raise serializers.ValidationError("Product quantity must be greater than 0.")
        return value

    def validate_unit_price(self, value):
        if value is None or value <= 0:
            raise serializers.ValidationError("Unit price must be greater than 0.")
        return value

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

    def validate_product_quantity(self, value):
        if value is None or value <= 0:
            raise serializers.ValidationError("Product quantity must be greater than 0.")
        return value

    def validate_unit_price(self, value):
        if value is None or value <= 0:
            raise serializers.ValidationError("Unit price must be greater than 0.")
        return value

class OrganizationPurchaseOrderSerializer(serializers.ModelSerializer):
    purchase_items = OrganizationPurchaseItemSerializer(many=True)

    class Meta:
        model = OrganizationPurchaseOrder
        fields = ['id','organization','total_quantities','total_items','supplier', 'purchase_date', 'payment_method', 'total_amount_paid', 'purchase_items']
        read_only_fields = ['id']

    def create(self, validated_data):
        purchase_items_data = validated_data.pop('purchase_items')
        total_quantities = 0
        total_items = 0
        total_price = 0
        purchase_order = OrganizationPurchaseOrder.objects.create(**validated_data)
        organization = validated_data['organization']
        for item_data in purchase_items_data:
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
        purchase_order.total_quantities = total_quantities
        purchase_order.total_items = total_items
        purchase_order.save()
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
