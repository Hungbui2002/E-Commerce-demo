from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from .models import Clothes
from product_service.utils import serializer
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
# Create your views here.
@csrf_exempt
@require_http_methods(["GET"])
def getclothes(request):
    clothes = Clothes.objects.all()
    data = serializer(clothes)
    return JsonResponse(data,safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def getClotheById(request):
    data = {}
    try:
        clothe_id = request.GET.get('product_id')
        clothe = Clothes.objects.get(product_id=clothe_id)
        data = clothe.to_json()
    except:
        pass
    return JsonResponse(data,safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def searchClothes(request):
    key = request.GET.get('key')
    category_id = request.GET.get('category_id')
    data = []
    try:
        books = Clothes.objects.filter(name__icontains=key, category_id=category_id)
        data = serializer(books)
    except:
        pass
    return JsonResponse(data,safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def getClothesByCategory(request):
    category_id = request.GET.get('category_id')
    data = []
    try:
        clothes = Clothes.objects.filter(category_id=category_id)
        data = serializer(clothes)
    except:
        pass
    return JsonResponse(data,safe=False)