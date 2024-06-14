from django.db import models
from django.conf import settings
from decimal import Decimal
import requests
from .utils import *

class CartItem(models.Model):
    customer_id = models.BigIntegerField(null=True)
    product_id = models.CharField(max_length=100,null = True)
    quantity = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=100,null = True,blank = True)

    def getProduct(self):
        product = getProduct(self.product_id)
        return product
    
    def getCustomer(self):
        customer = getCustomer(self.customer_id)
        return customer

    def getCategoryName(self):
        return self.getProduct().category.name
    
    def getFullNameCustomerOrder(self):
        return self.getCustomer().user.first_name + " "+self.getCustomer().user.last_name
        
    def getTotalPrice(self):
        product = self.getProduct()
        return float(str(product.price)) * self.quantity
    class Meta:
        # Đặt tên bảng mới ở đây
        db_table = 'Cart_item'
