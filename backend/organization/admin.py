from django.contrib import admin
from .models import (
    Organization,
    OrganizationUser,
    OrganizationSubscription,
    OrganizationInventory,
    OrganizationProduct,
    OrganizationBilling,
    OrganizationBillingItem,
    OrganizationPurchaseItem,
    OrganizationPurchaseOrder,
    Supplier,
    OrganizationOnBoarding,
)

@admin.register(OrganizationOnBoarding)
class OrganizationOnboardingAdmin(admin.ModelAdmin):
    list_display = (
        "email",
        "otp",
        "is_verified",
        "user_first_name",
        "user_last_name",
        "org_name",
        "org_address",
    )
    search_fields = ("email", "user_first_name", "user_last_name", "org_name")
    list_filter = ("is_verified",)  # <-- was a string before, should be a tuple

# Register remaining models
admin.site.register(Organization)
admin.site.register(OrganizationUser)
admin.site.register(OrganizationSubscription)
admin.site.register(OrganizationInventory)
admin.site.register(OrganizationProduct)
admin.site.register(OrganizationBilling)
admin.site.register(OrganizationBillingItem)
admin.site.register(OrganizationPurchaseItem)
admin.site.register(OrganizationPurchaseOrder)
admin.site.register(Supplier)