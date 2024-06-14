from django.http import JsonResponse
from .models import Mobile
from product_service.utils import serializer
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
# Create your views here.
@csrf_exempt
@require_http_methods(["GET"])
def getMobile(request):
    mobiles = Mobile.objects.all()
    data = serializer(mobiles)
    return JsonResponse(data,safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def getMobileById(request):
    data = {}
    try:
        mobile_id = request.GET.get('product_id')
        mobile = Mobile.objects.get(product_id=mobile_id)
        data = mobile.to_json()
    except:
        pass
    return JsonResponse(data,safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def searchMobile(request):
    key = request.GET.get('key')
    category_id = request.GET.get('category_id')
    data = []
    try:
        books = Mobile.objects.filter(name__icontains=key, category_id=category_id)
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
        mobiles = Mobile.objects.filter(category_id=category_id)
        data = serializer(mobiles)
    except:
        pass
    return JsonResponse(data,safe=False)