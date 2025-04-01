from rest_framework import serializers
from .models import Organization, OrganizationUser, OrganizationSubscription, OrganizationInventory, OrganizationProduct, OrganizationBilling, OrganizationBillingItem, OrganizationPurchaseItem, OrganizationPurchaseOrder


from rest_framework import serializers
from .models import Organization, OrganizationUser, OrganizationSubscription

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = ['id', 'org_name', 'org_address', 'org_logo', 'gst_number', 'has_gst_number']

class OrganizationUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationUser
        fields = ['user_email', 'user_role', 'is_active']

class OrganizationSubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationSubscription
        fields = ['plan_name', 'plan_price', 'start_date', 'end_date', 'status']

class OrganizationCreateSerializer(serializers.Serializer):
    organization = OrganizationSerializer()
    user = OrganizationUserSerializer()
    subscription = OrganizationSubscriptionSerializer()

    def create(self, validated_data):
        organization_data = validated_data.pop('organization')
        user_data = validated_data.pop('user')
        subscription_data = validated_data.pop('subscription')

        organization = Organization.objects.create(**organization_data)
        user = OrganizationUser.objects.create(organization=organization, **user_data)
        subscription = OrganizationSubscription.objects.create(organization=organization, **subscription_data)

        return {
            'organization': organization,
            'user': user,
            'subscription': subscription
        }

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['organization'] = OrganizationSerializer(instance['organization']).data
        data['user'] = OrganizationUserSerializer(instance['user']).data
        data['subscription'] = OrganizationSubscriptionSerializer(instance['subscription']).data
        return data

class OrganizationRetrieveSerializer(serializers.ModelSerializer):
    user = OrganizationUserSerializer()
    subscription = OrganizationSubscriptionSerializer()

    class Meta:
        model = Organization
        fields = ['id', 'org_name', 'org_address', 'org_logo', 'gst_number', 'has_gst_number', 'user', 'subscription']

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data['user'] = OrganizationUserSerializer(instance.organizationuser_set.first()).data
        data['subscription'] = OrganizationSubscriptionSerializer(instance.organizationsubscription_set.first()).data
        return data


class OrganizationInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationInventory
        fields = ['id', 'organization', 'product', 'product_code', 'quantity_in_stock', 'unit_price']

class OrganizationProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationProduct
        fields = ['id', 'organization', 'product_name']

class OrganizationBillingSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationBilling
        fields = ['organization', 'billing_id', 'payment_methode', 'total_quantities', 'total_items', 'total_price', 'total_tax', 'discount', 'tax_percentage', 'final_amount', 'status', 'gst_number']

class OrganizationBillingItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationBillingItem
        fields = ['id', 'item_name', 'quantity', 'unit_price', 'line_item_price']

class OrganizationPurchaseItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationPurchaseItem
        fields = ['id', 'organization', 'product', 'quantity', 'purchase_price', 'total_price', 'purchase_date']

class OrganizationPurchaseOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrganizationPurchaseOrder
        fields = ['id', 'organization', 'purchase_items', 'supplier', 'purchase_date', 'payment_method', 'total_amount_paid']