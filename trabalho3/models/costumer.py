from django.db import models


class Costumer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)

    class Meta:
        db_table = "costumer"
