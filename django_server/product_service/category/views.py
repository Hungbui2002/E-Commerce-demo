from django.shortcuts import render
import requests
# Create your views here.
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse

from product_service.utils import serializer
from django.views.decorators.csrf import csrf_exempt
from .models import Category

@require_http_methods(["GET"])
def getCategorys(request):
    categories = Category.objects.all()
    data = serializer(categories)
    return JsonResponse(data=data,safe=False)


@require_http_methods(["GET"])
def getProductByCategory(request):
    categories_data = Category.objects.all()
    categories = serializer(categories_data)
    category_items = []
    for category in categories:
        items = getProductByCategory(category['id'])
        # Thêm vào danh sách kết quả với danh mục và các items tương ứng
        category_items.append({
            'category': category,
            'items': items
        })
    return JsonResponse(data=category_items,safe=False)