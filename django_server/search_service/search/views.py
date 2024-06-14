from django.shortcuts import render,redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from imagehash import average_hash
from PIL import Image
from django.views.decorators.http import require_http_methods
# Create your views here.
import json
from django.core.files.storage import FileSystemStorage

from search.utils import *
import requests

# Create your views here.
@require_http_methods(["GET"])
def search_product_by_key(request):
    query = request.GET.get('search','')
    category_request = requests.get('http://127.0.0.1:8008/api/catalog/getCategories')
    categories = category_request.json() if category_request.status_code == 200 else []
    # Chuẩn bị dữ liệu cho mỗi danh mục
    category_items = []
    for category in categories:
        items = filterAPI(query,category['id'])
        category_items.append({
            'category': category,
            'items': items
        })
    context = {'category_items': category_items}
    return JsonResponse(context, safe=False)

def vocie_search(request):
    query = request.GET.get('search','')
    category_request = requests.get('http://127.0.0.1:8000/api/catalog/getCategories')
    categories = category_request.json() if category_request.status_code == 200 else []
    # Chuẩn bị dữ liệu cho mỗi danh mục
    category_items = []
    for category in categories:
        items = filterAPI(query,category['id'])
        category_dict = {
            'id':category.id,
            'name':category.name,
            'type_product':category.type_product
        }
        items_list = toDict(items)
        category_items.append({
            'category': category_dict,
            'items': items_list
        })
    return JsonResponse(category_items, safe=False)


# def search_product_by_image(request):
#     if request.method == 'POST':
#         form = ImageUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             image = request.FILES['image']
#             fs = FileSystemStorage()
#             filename = fs.save(image.name, image)
#             uploaded_image_path = fs.path(filename)
            
#             # Mở và tính hash cho hình ảnh được tải lên
#             uploaded_image = Image.open(uploaded_image_path)
#             uploaded_hash = average_hash(uploaded_image)
            
#             # So sánh với các hình ảnh sản phẩm trong cơ sở dữ liệu
#             similar_products = []
#             product_response = requests.get('http://127.0.0.1:8000/api/product/get_products')
#             products = product_response.json() if product_response.status_code == 200 else []

#             for product in products:
#                 product_image_path = product['image_path']
#                 product_image = Image.open(product_image_path)
#                 product_hash = average_hash(product_image)
                
#                 # So sánh hash; bạn có thể điều chỉnh ngưỡng
#                 if abs(uploaded_hash - product_hash) < 3:  # Ngưỡng này có thể điều chỉnh
#                     similar_products.append(product)
            
#             category_request = requests.get('http://127.0.0.1:8000/api/catalog/getCategories')
#             categories = category_request.json() if category_request.status_code == 200 else []
#             category_items = []
#             for category in categories:
#                 items = filterByCategory(similar_products,category['id'])
#                 category_items.append({
#                     'category': category,
#                     'items': items
#                 })
#             # Xóa file tạm sau khi xử lý
#             fs.delete(filename)
#             return render(request, 'home_product.html', {'category_items': category_items})
#     else:
#         form = ImageUploadForm()
#     return render(request, 'home_product.html', {'form': form})

