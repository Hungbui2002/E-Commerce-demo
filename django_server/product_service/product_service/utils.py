from book.models import Book
from mobile.models import Mobile
from clothes.models import Clothes

def serializer(data):
    return [item.to_json() for item in data]

def getListProductByCategory(category_id):
    products_in_category = Mobile.objects.filter(category_id=category_id)
    books_in_category = Book.objects.filter(category_id=category_id)
    clothes_in_category = Clothes.objects.filter(category_id=category_id)
    items = list(products_in_category) + list(books_in_category) + list(clothes_in_category)
    return items
