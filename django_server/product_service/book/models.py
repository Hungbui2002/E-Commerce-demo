from category.models import Category
import json
from django.db import models
import uuid
from django.db.models import Max
# Create your models here.
class Author(models.Model):
    author_id = models.IntegerField(unique=True, editable=False)
    name = models.CharField(max_length=100)
    address = models.TextField(null = True,blank=True)
    email = models.EmailField(null = True,blank=True)

    def save(self, *args, **kwargs):
        if not self.author_id:
            self.author_id = self.nextId()
        super(Author,self).save(*args, **kwargs)
    
    def nextId(self):
        result = Author.objects.all().aggregate(max_id=Max('author_id'))
        max_id = result.get('max_id')  # Sẽ trả về None nếu không có bản ghi nào
        return (max_id + 1) if max_id is not None else 0  # Trả về 0 nếu không tìm thấy giá trị


    def __str__(self):
        return self.name

class Publisher(models.Model):
    publisher_id = models.IntegerField(unique=True, editable=False)
    name = models.CharField(max_length=100)
    address = models.TextField(null = True,blank=True)
    email = models.EmailField(null = True,blank=True)

    def save(self, *args, **kwargs):
        if not self.publisher_id:
            self.publisher_id = self.nextId()
        super(Publisher,self).save(*args, **kwargs)
    
    def nextId(self):
        result = Publisher.objects.all().aggregate(max_id=Max('publisher_id'))
        max_id = result.get('max_id')  # Sẽ trả về None nếu không có bản ghi nào
        return (max_id + 1) if max_id is not None else 0  # Trả về 0 nếu không tìm thấy giá trị
    
    def __str__(self):
        return self.name
    
class Book(models.Model):
    product_id = models.CharField(max_length=100, unique=True, blank=True, editable=False)
    name = models.CharField(max_length=100)
    author_id = models.IntegerField(blank=True,null= True)
    publisher_id = models.IntegerField(blank=True,null= True)
    description = models.TextField(blank=True,null = True)
    price = models.DecimalField(max_digits=10, decimal_places=2,null = True)
    image = models.TextField(blank=True,null = True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    category_id = models.IntegerField(null = True)
    quantity = models.IntegerField(null = True)

    def save(self, *args, **kwargs):
        if not self.product_id:  # Kiểm tra nếu product_id chưa được tạo
            # Tạo product_id bằng cách kết hợp 'B' với một UUID mới
            self.product_id = 'B' + str(uuid.uuid4())
        super(Book, self).save(*args, **kwargs)  # Gọi phương thức save gốc của Django

    def getAuthor(self):
        author = Author.objects.filter(author_id = self.author_id).first()
        return author
    
    def getPublisher(self):
        return Publisher.objects.filter(publisher_id = self.publisher_id).first()
    
    def getCategory(self):
        return Category.objects.filter(category_id = self.category_id).first()
    
    def to_json(self):
        product_data = {
            'product_id': self.product_id,
            'name': self.name,
            'author':self.getAuthor().name if self.getAuthor() else None,   
            'publisher':self.getPublisher().name if self.getPublisher() else None,   
            'price': str(self.price),  # Chuyển đổi thành chuỗi để đảm bảo định dạng JSON
            'description': self.description,
            'image': self.image if self.image else None,  # Lấy URL của hình ảnh nếu có
            'category_id': self.category_id,
        }
        # Chuyển đổi từ điển thành chuỗi JSON
        # product_json = json.dumps(product_data)
        return product_data

    def __str__(self):
        return self.name