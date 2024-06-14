from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Order,Voucher
from .serializers import OrderSerializer,VoucherSerializer

@api_view(['POST'])
def create_order(request):
    order_serializer = OrderSerializer(data=request.data)
    status = {}
    if order_serializer.is_valid():
        order_serializer.save()
        status = {
            'status':1
        }
        return Response(status, status=status.HTTP_201_CREATED)
    status = {
        'status':0
    }
    return Response(status, status=status.HTTP_400_BAD_REQUEST)

@api_view(["GET"])
def get_order(request):
    try:
        customer_id = request.GET.get('customer_id', None)
        if customer_id is not None:
            orders = Order.objects.filter(customer_id=customer_id)
            order_serializer = OrderSerializer(orders, many=True)
            return Response(order_serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "customer_id is required"}, status=status.HTTP_400_BAD_REQUEST)
    except Order.DoesNotExist:
        return Response({"error": "No orders found for the given customer_id"}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['PUT'])
def update_order(request):
    try:
        order = Order.objects.get(pk=request.data['id'])
    except Order.DoesNotExist:
        return Response({'error': 'Order not found'}, status=status.HTTP_404_NOT_FOUND)
    
    order_serializer = OrderSerializer(order, data=request.data)
    
    if order_serializer.is_valid():
        order_serializer.save()
        return Response(order_serializer.data, status=status.HTTP_200_OK)
    
    return Response(order_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def delete_order(request, order_id):
    try:
        order = Order.objects.get(pk=order_id)
    except Order.DoesNotExist:
        return Response({'status': 404}, status=status.HTTP_404_NOT_FOUND)
    if order.status != 'Đang chuẩn bị đơn':
        return Response({'status': 2}, status=status.HTTP_200_OK)
    order.delete()
    return Response({'status': 1}, status=status.HTTP_200_OK)


@api_view(['GET'])
def list_voucher(request):
    vouchers = Voucher.objects.all()
    voucher_serializer = VoucherSerializer(vouchers, many=True)
    return Response(voucher_serializer.data, status=status.HTTP_200_OK)