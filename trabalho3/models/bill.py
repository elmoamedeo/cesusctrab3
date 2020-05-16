from django.db import models
from ..models import costumer, provider


class Bill(models.Model):
    price = models.CharField(max_length=10)
    costumer = models.ForeignKey(costumer.Costumer, on_delete=models.CASCADE)
    provider = models.ForeignKey(provider.Provider, on_delete=models.CASCADE)

    class Meta:
        db_table = "bill"
