# forms.py

from django import forms
from .models import Clothes


class ClothesForm(forms.ModelForm):
    class Meta:
        model = Clothes
        fields = ['name', 'description', 'price', 'image','category','brand','color','size']


        
