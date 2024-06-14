from django.db import models

TYPE_CHOICES = (
        ('freeship', 'Freeship'),
        ('discount', 'Discount'),
    )

# Create your models here.
class Voucher(models.Model):
    name = models.CharField(max_length=255)
    discount=models.FloatField(null= False)
    condition = models.IntegerField(default=0)
    type = models.CharField(max_length=100, choices=TYPE_CHOICES, null=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    customer_id = models.IntegerField(null= False)
    attribute = models.CharField(max_length=255)
    discount = models.FloatField(default=0)
    voucher = models.ForeignKey(Voucher, on_delete=models.CASCADE)
    payment_id = models.IntegerField(null= False)
    shipment_id = models.IntegerField(blank=True,null=True)
    status = models.CharField(max_length=100)
    estimated_delivery_date = models.DateField(blank=True, null=True)
    delivery_date = models.DateField(blank=True, null=True)


class OrderItem(models.Model):
    product_id = models.CharField(max_length=100, unique=True, blank=True)
    quantity = models.IntegerField()
    price = models.FloatField()
    order = models.ForeignKey(Order, on_delete=models.CASCADE)