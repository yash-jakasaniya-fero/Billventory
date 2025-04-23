from django.contrib import admin
from .models import Organization, OrganizationUser, OrganizationSubscription, OrganizationInventory, OrganizationProduct, OrganizationBilling, OrganizationBillingItem, OrganizationPurchaseItem,OrganizationPurchaseOrder, Supplier, OrganizationOnBoarding

# Register your models here.
admin.site.register(OrganizationOnBoarding)
admin.site.register(Organization)
admin.site.register(OrganizationUser)
admin.site.register(OrganizationSubscription)
admin.site.register(OrganizationInventory)
admin.site.register(OrganizationBilling)
admin.site.register(OrganizationPurchaseOrder)
admin.site.register(Supplier)