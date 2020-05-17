from django.db import models
from ..models import provider, product


class ProviderBill(models.Model):
    quantity = models.IntegerField()
    provider = models.ForeignKey(provider.Provider, on_delete=models.CASCADE, default='null')
    product = models.ManyToManyField(product.Product, default='null')

    class Meta:
        db_table = "provider_bill"

