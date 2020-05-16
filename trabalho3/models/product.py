from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=5)

    class Meta:
        db_table = "product"
