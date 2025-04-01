from rest_framework import serializers
from .models import Subscription, Supplier

class SupplierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Supplier
        fields = ['supplier_code','email','gst_number','name','contact_person','address']

class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = ['subscription_type', 'price', 'duration_days']

    def validate(self, data):
        subscription_type = data.get('subscription_type')

        if subscription_type == Subscription.DIAMOND:
            data['price'] = 1000
            data['duration_days'] = 30
        elif subscription_type == Subscription.PLATINUM:
            data['price'] = 700
            data['duration_days'] = 30
        elif subscription_type == Subscription.GOLD:
            data['price'] = 500
            data['duration_days'] = 30

        return data
