from django.contrib import admin
from django.db import models
from .models import Organization, OrganizationUser, OrganizationSubscription, OrganizationInventory, OrganizationProduct, OrganizationBilling, OrganizationBillingItem, OrganizationPurchaseItem,OrganizationPurchaseOrder, Supplier, OrganizationOnBoarding

@admin.register(models.OrganizationOnBoarding)
class OrganizationOnboardingAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "otp",
        "is_verified",
        "user_first_name", "user_last_name", "org_name", "org_address"
    )

    search_fields = ("email", "user_first_name", "user_last_name", "org_name")
    list_filter ="is_verified"
# Register your models here.
admin.site.register(OrganizationOnboardingAdmin, OrganizationOnBoarding)
admin.site.register(Organization)
admin.site.register(OrganizationUser)
admin.site.register(OrganizationSubscription)
admin.site.register(OrganizationInventory)
admin.site.register(OrganizationBilling)
admin.site.register(OrganizationPurchaseOrder)
admin.site.register(Supplier)