from django.db import models
from lib.models import BaseModel

class Supplier(BaseModel):
    supplier_code = models.CharField(max_length=255, unique=True, blank=True, null=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    gst_number = models.CharField(max_length=15, blank=True, null=True)
    name = models.CharField(max_length=255)
    contact_person = models.CharField(max_length=255, blank=True, null=True)
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Subscription(models.Model):
    DIAMOND = 'Diamond'
    PLATINUM = 'Platinum'
    GOLD = 'Gold'

    SUBSCRIPTION_CHOICES = [
        (DIAMOND, 'Diamond'),
        (PLATINUM, 'Platinum'),
        (GOLD, 'Gold'),
    ]

    subscription_type = models.CharField(max_length=50, choices=SUBSCRIPTION_CHOICES)
    price = models.IntegerField()
    duration_days = models.IntegerField()
