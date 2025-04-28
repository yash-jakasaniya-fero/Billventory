import random
import string
from email.policy import default
from django.utils import timezone
from datetime import timedelta
from django.db import models
import uuid
from lib.models import BaseModel
from lib.choices import RoleChoices, StatusChoices, PaymentMethodChoices


class OrganizationOnBoarding(BaseModel):
    email = models.EmailField(unique=True)
    otp = models.CharField(max_length=6)
    is_verified = models.BooleanField(default=False,blank=True, null=True)
    user_first_name = models.CharField(max_length=25,blank=True, null=True)
    user_last_name = models.CharField(max_length=25,blank=True, null=True)
    org_name = models.CharField(max_length=255,blank=True, null=True)
    org_address = models.CharField(max_length=255,blank=True, null=True)
    gst_number = models.CharField(max_length=15,blank=True, null=True)
    organization = models.ForeignKey("Organization", related_name='organization_onboarding',on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.org_name

class OrganizationUser(BaseModel):
    user_first_name = models.CharField(max_length=25, blank=True, null=True)
    user_last_name = models.CharField(max_length=25, blank=True, null=True)
    user_email = models.EmailField(unique=True)
    user_role = models.CharField(choices=RoleChoices.choices, max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ['user_email']


class Organization(BaseModel):
    org_id = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(OrganizationUser, related_name='organization_user', on_delete=models.CASCADE)
    org_name = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    org_logo = models.ImageField(blank=True, null=True)
    gst_number = models.CharField(max_length=15, blank=True, null=True)


class OrganizationSubscription(BaseModel):
    organization = models.ForeignKey(Organization, related_name='organization_subscriptions', on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    plan_price = models.PositiveIntegerField(default=0)
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    status = models.CharField(choices=StatusChoices.choices, max_length=50)


class Supplier(BaseModel):
    supplier_code = models.CharField(max_length=255, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    gst_number = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class OrganizationInventory(BaseModel):
    organization = models.ForeignKey(Organization, related_name='organization_inventories', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity_in_stock = models.PositiveIntegerField(default=0)


class OrganizationProduct(BaseModel):
    product_name = models.CharField(max_length=100)


class OrganizationBilling(BaseModel):
    organization = models.ForeignKey(Organization, related_name='organization_billing', on_delete=models.CASCADE)
    billing_id = models.CharField(max_length=20, unique=True, blank=True)
    payment_method = models.CharField(choices=PaymentMethodChoices.choices, max_length=50, default=True)
    total_quantities = models.PositiveIntegerField(default=0)
    total_items = models.PositiveIntegerField(default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    total_tax = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    discount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2,default=0)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2,default=0)
    gst_number = models.CharField(max_length=15, blank=True, null=True)

    # def generate_billing_id(self):
    #     random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    #     return f"BILL-{random_string}"

class OrganizationBillingItem(BaseModel):
    billing = models.ForeignKey(OrganizationBilling, related_name='billing_items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=255)
    product_quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_item_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)

class OrganizationPurchaseOrder(BaseModel):
    organization = models.ForeignKey(Organization, related_name='organization_purchase_order', on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, related_name='purchase_orders', on_delete=models.CASCADE)
    total_quantities = models.PositiveIntegerField(default=0)
    total_items = models.PositiveIntegerField(default=0)
    purchase_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(choices=PaymentMethodChoices.choices, max_length=50, default=True)
    total_amount_paid = models.DecimalField(max_digits=15, decimal_places=2,default=0)

class OrganizationPurchaseItem(BaseModel):
    purchase_order = models.ForeignKey(OrganizationPurchaseOrder, related_name='purchase_items', on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_quantity = models.PositiveIntegerField(default=0)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    line_item_price = models.DecimalField(max_digits=15, decimal_places=2,default=0)


class OrganizationNotification(BaseModel):
    organization = models.ForeignKey(Organization, related_name='organization_notifications', on_delete=models.CASCADE)
    message = models.TextField()