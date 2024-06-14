from django.shortcuts import render
from rest_framework import status as drf_status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Shipment
from .serializers import  ShipmentSerializer
# Create your views here.

@api_view(['GET'])
def list_shipments(request):
    shipments = Shipment.objects.all()
    shipment_serializer = ShipmentSerializer(shipments, many=True)
    return Response(shipment_serializer.data, status=drf_status.HTTP_200_OK)