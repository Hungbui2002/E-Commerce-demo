from django.db import models
from django.conf import settings
from django.contrib.auth.models import User

class Customer(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="customer")
    phone = models.CharField(max_length=10)
    address = models.CharField(max_length=255, blank=True, null=True)
    # Add any additional fields or methods as needed
    @classmethod
    def authenticate_customer(cls, username, password):
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        if user.check_password(password) and hasattr(user, 'customer'):
            return user.customer
        else:
            return None
    
    def toJson(self):
        customer_data = {
            'id': self.id,
            'first_name': self.user.first_name,
            'last_name': self.user.last_name,
            'full_name': self.user.last_name + ' '+self.user.first_name,
            'phone': self.phone,
            'address': self.address
        }
        return customer_data
        
    def __str__(self):
        return self.name
