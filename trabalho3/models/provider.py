from django.db import models


class Provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    number = models.CharField(max_length=15)

    class Meta:
        db_table = "provider"

    def __str__(self):
        return self.name
