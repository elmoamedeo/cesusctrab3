from django.db import models
from ..models import costumer


class Bill(models.Model):
    price = models.CharField(max_length=10)
    costumer = models.ForeignKey(costumer.Costumer, on_delete=models.CASCADE, default='null')

    class Meta:
        db_table = "bill"
