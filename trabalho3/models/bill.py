from django.db import models


class Bill(models.Model):
    price = models.CharField(max_length=10)

    class Meta:
        db_table = "bill"
