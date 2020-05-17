from django.db import models
from ..models import provider


class Employee(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    neighborhood = models.CharField(max_length=100)
    address_number = models.IntegerField(max_length=10)
    email = models.EmailField()
    number = models.CharField(max_length=15)
    provider = models.ForeignKey(provider.Provider, on_delete=models.CASCADE, default='null')

    class Meta:
        db_table = "employee"
