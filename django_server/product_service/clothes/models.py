from category.models import Category
import json
from django.db import models
import uuid
from django.db.models import Max

class Producer(models.Model):
    producer_id = models.IntegerField(unique=True,editable=False)
    name = models.CharField(max_length=100)
    address = models.TextField(null = True,blank=True)
    email = models.EmailField(null = True,blank=True)

    def save(self, *args, **kwargs):
        if not self.producer_id:
            self.producer_id = self.nextId()
        super(Producer,self).save(*args, **kwargs)
    
    def nextId(self):
        result = Producer.objects.all().aggregate(max_id=Max('producer_id'))
        max_id = result.get('max_id')  # Sẽ trả về None nếu không có bản ghi nào
        return (max_id + 1) if max_id is not None else 0  # Trả về 0 nếu không tìm thấy giá trị
    
    def __str__(self):
        return self.name

class Styles(models.Model):
    style_id = models.IntegerField(unique=True,editable=False)
    name = models.CharField(max_length=100)
    size = models.CharField(max_length=10)
    color = models.CharField(max_length=50,blank=True)

    def save(self, *args, **kwargs):
        if not self.style_id:
            self.style_id = self.nextId()
        super(Styles,self).save(*args, **kwargs)
    
    def nextId(self):
        result = Styles.objects.all().aggregate(max_id=Max('style_id'))
        max_id = result.get('max_id')  # Sẽ trả về None nếu không có bản ghi nào
        return (max_id + 1) if max_id is not None else 0  # Trả về 0 nếu không tìm thấy giá trị

    def __str__(self):
        return self.name
    
# Create your models here.
class Clothes(models.Model):
    product_id = models.CharField(max_length=100, unique=True, blank=True, editable=False)
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=100,blank=True)
    description = models.TextField(blank=True,null = True)
    image = models.TextField(blank=True,null = True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category_id = models.IntegerField(null = True)
    quantity = models.IntegerField(null = True)
    producer_id =models.IntegerField(null = True)
    style_id = models.IntegerField(null = True)

    def save(self, *args, **kwargs):
        if not self.product_id:  # Kiểm tra nếu product_id chưa được tạo
            # Tạo product_id bằng cách kết hợp 'B' với một UUID mới
            self.product_id = 'C' + str(uuid.uuid4())
        super(Clothes, self).save(*args, **kwargs)  # Gọi phương thức save gốc của Django

    def getProducer(self):
        return Producer.objects.filter(producer_id = self.producer_id).first()
    
    def getStyle(self):
        return Styles.objects.filter(style_id = self.style_id).first()
    def getCategory(self):
        return Category.objects.filter(category_id = self.category_id).first()
    
    def to_json(self):
        product_data = {
            'product_id': self.product_id,
            'name': self.name,
            'brand':self.brand,
            'color': self.getStyle().color if self.getStyle() else None,   
            'size': self.getStyle().size if self.getStyle() else None,   
            'price': str(self.price),  # Chuyển đổi thành chuỗi để đảm bảo định dạng JSON
            'description': self.description,
            'image': self.image if self.image else None,  # Lấy URL của hình ảnh nếu có
            'category_id': self.category_id,
            'type_product': self.getCategory().name
        }

        # Chuyển đổi từ điển thành chuỗi JSON
        # product_json = json.dumps(product_data)
        return product_data

    def __str__(self):
        return self.name
