from django.db import models
from ..models import costumer, product


class CostumerBill(models.Model):
    quantity = models.IntegerField()
    costumer = models.ForeignKey(costumer.Costumer, on_delete=models.CASCADE, default='null')
    product = models.ManyToManyField(product.Product, default='null')

    class Meta:
        db_table = "costumer_bill"

    def __str__(self):
        return self.name
