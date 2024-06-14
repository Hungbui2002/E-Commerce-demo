from django.db import models
import uuid
from django.db.models import Max

# Create your models here.
TYPE_CHOICES = (
        ('Phone', 'Phone'),
        ('Book', 'Book'),
        ('Clothes', 'Clothes'),
    )

class Category(models.Model):
    category_id = models.IntegerField(primary_key=True,unique=True,editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True,null = True)
    type_product = models.CharField(max_length=100, choices=TYPE_CHOICES, null=True)


    def save(self, *args, **kwargs):
        if not self.category_id:
            self.category_id = self.nextId()
        super(Category,self).save(*args, **kwargs)
    
    def nextId(self):
        result = Category.objects.all().aggregate(max_id=Max('category_id'))
        max_id = result.get('max_id')  # Sẽ trả về None nếu không có bản ghi nào
        return (max_id + 1) if max_id is not None else 0  # Trả về 0 nếu không tìm thấy giá trị
    
    def to_json(self):
        data = {
            'id':self.category_id,
            'name':self.name,
            'type_product':self.type_product
        }
        return data

    def __str__(self):
        return self.name
    
