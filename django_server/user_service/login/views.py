from django.shortcuts import render
from .models import Customer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
from django.views.decorators.http import require_http_methods
import json

# Tạo một logger instance
logger = logging.getLogger(__name__)
# Create your views here.

@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username,password = data['username'],data['password']
        customer = Customer.authenticate_customer(username,password)
        if customer == None:
            response = {
                'status':0,
                'description': 'wrong username password'
            }
        else:
            response = {
                'status':1,
                'customer':customer.toJson()
            }
            
        return JsonResponse(response,safe=False)


        