from django.db import models

# Create your models here.
class Shipment(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    price = models.FloatField()

    def __str__(self):
        return self.tracking_number