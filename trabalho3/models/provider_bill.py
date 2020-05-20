from django.db import models
from ..models import provider, product


class ProviderBill(models.Model):
    quantity = models.IntegerField()
    product = models.ManyToManyField(product.Product, default='null')

    class Meta:
        db_table = "provider_bill"

