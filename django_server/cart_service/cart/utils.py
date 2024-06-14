
import requests
from cart_service.settings import API_GET_CUSTOMER_INF, API_GET_BOOK_ID,API_GET_CLOTHES_ID,API_GET_MOBILE_ID

def itemCartJson(items):
    data = []
    for item in items:
        product = item.getProduct()
        item_json = {
            'id': item.id,
            'product': {
                'product_id': item.product_id,
                'name': product['name'],
                'price': product['price'],
                'image': product['image'],
            },
            'quantity': item.quantity,
            'status': item.status,
            'type_product': product['type_product'] 
        }
        data.append(item_json)
    return data

def getProduct(product_id):
    try:
        book_response = requests.get(f'{API_GET_BOOK_ID}{product_id}')
        books = book_response.json() if book_response.status_code == 200 else []
        if books: return books
        mobile_response = requests.get(f'{API_GET_MOBILE_ID}{product_id}')
        mobiles = mobile_response.json() if mobile_response.status_code == 200 else []
        if mobiles: return mobiles

        clothes_response = requests.get(f'{API_GET_CLOTHES_ID}{product_id}')
        clothes = clothes_response.json() if clothes_response.status_code == 200 else []
        if clothes: return clothes

        return {}

    except requests.RequestException as e:
        print(e)
        return {}

def getCustomer(customer_id):
    customer = requests.get(f'{API_GET_CUSTOMER_INF}{customer_id}')
    return customer