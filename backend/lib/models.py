from django.db import models
from model_utils.models import TimeStampedModel

class BaseModel(TimeStampedModel):
    ORDERING = ("-created", "-modified")
    added_by = models.CharField(verbose_name="Added by", max_length=100, blank=True, null=True)
    updated_by = models.CharField(verbose_name="Updated by", max_length=100, blank=True, null=True)

    class Meta:
        abstract = True
