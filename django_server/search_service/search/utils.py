
from django.http import JsonResponse
import requests



def filterAPI(key,category_id):
    print(key,category_id)
    book_response = requests.get(f'http://127.0.0.1:8008/api/book/search?key={key}&category_id={category_id}')
    books = book_response.json() if book_response.status_code == 200 else []

    mobile_response = requests.get(f'http://127.0.0.1:8008/api/mobile/search?key={key}&category_id={category_id}')
    mobiles = mobile_response.json() if mobile_response.status_code == 200 else []

    clothes_response = requests.get(f'http://127.0.0.1:8008/api/clothes/search?key={key}&category_id={category_id}')
    clothes = clothes_response.json() if clothes_response.status_code == 200 else []
    products = books + mobiles + clothes
    return products


def filterByCategory(products, category_id):
    items = []
    for product in products:
        if int(product['category_id']) == category_id:
            items.append(product)
    return items


def objectToDict(product):
    product_dict = {
        'id': product.id,
        'name': product.name,
        'description': product.description,
        'price': float(str(product.price)),
        'image': product.image.url,
        'category_id': product.category_id,
    }
    return product_dict

def toDict(items):
    products = []
    for item in items:
        products.append(objectToDict(item))
    return products

