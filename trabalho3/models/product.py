from django.db import models
from ..models import provider


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.IntegerField(max_length=5)
    provider = models.ForeignKey(provider.Provider, on_delete=models.CASCADE, default='null')

    class Meta:
        db_table = "product"
