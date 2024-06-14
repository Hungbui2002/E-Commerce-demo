from django.shortcuts import render,redirect
from .models import CartItem
import json
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .utils import *
from django.views.decorators.csrf import csrf_exempt
# from .serializes import *
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.decorators import api_view
# Create your views here.
#api
# @api_view(['GET'])
@csrf_exempt
@require_http_methods(["GET"])
def get_cart_items(request):
    json_data = []
    try:
        customer_id = request.GET['customer_id']
        print(customer_id)
        if customer_id:
            items = CartItem.objects.filter(customer_id= customer_id)
            json_data = itemCartJson(items)
    except Exception as e:
        print(e)
    return JsonResponse(json_data,safe=False)


@require_http_methods(["GET"])
def remove_item(request,cart_id):
    response = {}
    try:
        item = CartItem.objects.get(id=cart_id)
        item.delete()
        response = {"status": 1}
    except:
        response = {"status": 0}
    return JsonResponse(response,safe=False)

@csrf_exempt
@require_http_methods(["POST"])
def save_item(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        print(data)
        res = {}
        try:
            item = CartItem.objects.get(id=data['id'])
            item.quantity = data['quantity']
            item.status = data['status']
            item.save()
            res = {'status':'OK'}
        except:
            res= {'status':'False'}
        return JsonResponse(res)
    
@csrf_exempt
@require_http_methods(["POST"])
def add_to_cart(request):
    data = {}
    if request.method == 'POST':
        json_data = json.loads(request.body.decode('utf-8'))
        try:
            cart_item = CartItem.objects.create(
                product_id=json_data.get('product_id'), # Truyền vào product_id thay vì product
                quantity=json_data.get('quantity', 1),
                status='Đợi mua hàng',
                customer_id=json_data['customer_id']
            )
            cart_item.save()
            data = {
                'message': 'Thêm sản phẩm vào giỏ hàng thành công',
                'status':1
            }
        except Exception as e:
            print(e)
            data = {
                'message': 'Có lỗi xảy ra',
                'status':0
            }
    return JsonResponse(data)