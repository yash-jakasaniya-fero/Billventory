from django.db import models
import uuid
from django.contrib.auth.models import User
from lib.models import BaseModel
from core.models import Supplier


class Organization(BaseModel):
    org_id = models.UUIDField(default=uuid.uuid4, editable=False)
    org_name = models.CharField(max_length=255)
    org_address = models.CharField(max_length=255)
    org_logo = models.ImageField(blank=True, null=True)
    gst_number = models.BooleanField(max_length=15, blank=True, null=True)
    has_gst_number = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.has_gst_number and not self.gst_number:
            raise ValueError("GST provided if has_gst_number")
        super().save(*args, **kwargs)

class OrganizationUser(BaseModel):
    ROLE_CHOICES=[
        ('Owner','Owner'),
        ('Manager','Manager'),
        ('Admin','Admin'),
    ]
    organization = models.ForeignKey(Organization, related_name='organization_users', on_delete=models.CASCADE)
    org_user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_email = models.EmailField(unique=True)
    user_role = models.CharField(choices=ROLE_CHOICES,max_length=50)
    is_active = models.BooleanField(default=True)

    class Meta:
        unique_together = ['org_user']


class OrganizationSubscription(BaseModel):
    STATUS_CHOICES=[
        ('Active','Active'),
        ('Expired','Expired'),
    ]
    organization = models.ForeignKey(Organization, related_name='organization_subscriptions', on_delete=models.CASCADE)
    plan_name = models.CharField(max_length=100)
    plan_price = models.PositiveIntegerField
    start_date = models.DateTimeField(auto_now_add=True)
    end_date = models.DateTimeField()
    status = models.CharField(choices=STATUS_CHOICES,max_length=50)



class OrganizationInventory(BaseModel):
    organization = models.ForeignKey(Organization, related_name='organization_inventories', on_delete=models.CASCADE)
    product = models.CharField(max_length=255)
    product_code = models.CharField(max_length=100, unique=True)
    quantity_in_stock = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)


class OrganizationProduct(BaseModel):
    organization = models.ForeignKey(Organization, related_name='organization_products', on_delete=models.CASCADE)
    product_name = models.ForeignKey(OrganizationInventory, related_name='product_name', on_delete=models.CASCADE)


class OrganizationBillingItem(BaseModel):
    item_name = models.CharField(max_length=255)
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    line_item_price = models.DecimalField(max_digits=10, decimal_places=2, editable=False)

    def save(self, *args, **kwargs):
        self.line_item_price = self.quantity * self.unit_price
        super().save(*args, **kwargs)


class OrganizationBilling(BaseModel):
    PAYMENT_CHOICES=[
        ('Cash','Cash'),
        ('Online','Online'),
    ]
    organization = models.ForeignKey(Organization, related_name='organization_billing', on_delete=models.CASCADE)
    billing_id = models.AutoField(primary_key=True , editable=False)
    payment_methode = models.CharField(choices=PAYMENT_CHOICES, max_length=50)
    total_quantities = models.PositiveIntegerField()
    total_items = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_tax = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=10, decimal_places=2)
    tax_percentage = models.DecimalField(max_digits=5, decimal_places=2)
    final_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField

    gst_number = models.CharField(max_length=15, blank=True, null=True)

    def save(self, *args, **kwargs):
        if self.organization.has_gst_number and not self.gst_number:
            raise ValueError("GST number is required if organizations have GST number.")
        elif not self.organization.has_gst_number and self.gst_number:
            self.gst_number = None
        super().save(*args, **kwargs)


class OrganizationPurchaseItem(BaseModel):
    organization = models.ForeignKey(Organization, related_name='organization_purchases', on_delete=models.CASCADE)
    product = models.ForeignKey(OrganizationInventory, related_name='product_purchases', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2)
    total_price = models.DecimalField(max_digits=15, decimal_places=2)
    purchase_date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.total_price = self.purchase_price * self.quantity
        super().save(*args, **kwargs)

class OrganizationPurchaseOrder(BaseModel):
    organization = models.ForeignKey(Organization, related_name='purchase_orders', on_delete=models.CASCADE)
    purchase_items = models.ManyToManyField(OrganizationPurchaseItem, related_name='purchase_orders')
    supplier = models.ForeignKey(Supplier,related_name='supplier_name', on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)
    payment_method = models.CharField(max_length=50)
    total_amount_paid = models.DecimalField(max_digits=15, decimal_places=2)

    def save(self, *args, **kwargs):
        self.total_amount_paid = sum(item.total_price for item in self.purchase_items.all())
        super().save(*args, **kwargs)

class OrganizationNotification(BaseModel):
    organization = models.ForeignKey(Organization, related_name='organization_notifications', on_delete=models.CASCADE)
    message = models.TextField()

