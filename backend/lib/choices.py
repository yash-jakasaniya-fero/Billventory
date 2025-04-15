from django.db import models

class RoleChoices(models.TextChoices):
    OWNER = 'Owner'
    MANAGER = 'Manager'
    ADMIN = 'Admin'

class StatusChoices(models.TextChoices):
    ACTIVE = 'Active'
    EXPIRED = 'Expired'

class PaymentMethodChoices(models.TextChoices):
    CASH = 'Cash'
    ONLINE = 'Online'

class SubscriptionChoices(models.TextChoices):
    DIAMOND = 'Diamond'
    PLATINUM = 'Platinum'
    GOLD = 'Gold'