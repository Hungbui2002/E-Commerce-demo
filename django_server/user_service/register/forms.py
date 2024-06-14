from django import forms
from django.contrib.auth.models import User
from login.models import Customer

class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password', 'first_name', 'last_name', 'email']

class CustomerRegistrationForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['phone', 'address']
