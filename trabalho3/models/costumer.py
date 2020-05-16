from django.db import models


class Costumer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    address_number = models.IntegerField(max_length=10)
    email = models.EmailField()
    number = models.CharField(max_length=15)

    class Meta:
        db_table = "costumer"
