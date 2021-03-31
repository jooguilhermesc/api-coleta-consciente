from django.db import models
from uuid import uuid4


class Recycle(models.Model):
    id_recycle_point = models.UUIDField(primary_key=True,default=uuid4,editable=False)
    category_recycle_point = models.CharField(max_length=255)
    name_recycle_point = models.CharField(max_length=255)
    end_recycle_point = models.CharField(max_length=255)
    latitude = models.FloatField(max_length=255)
    longitude = models.FloatField(max_length=255)
    category_recycle_procedure = models.CharField(max_length=255)
    contact_recycle_point = models.CharField(max_length=255)
    info_recycle_point = models.CharField(max_length=255)
    created_at = models.DateField(auto_now_add=True)
