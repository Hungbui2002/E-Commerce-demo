from django.shortcuts import render
from login.models import Customer
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import logging
from django.views.decorators.http import require_http_methods

# Tạo một logger instance
logger = logging.getLogger(__name__)
# Create your views here.

@csrf_exempt
@require_http_methods(["GET"])
def getCustomer(request):
    data = {}
    try:
        customer_id = request.GET.get('customer_id')
        print(customer_id)
        customer = Customer.objects.get(id=customer_id)
        data = customer.toJson()
    except:
        pass
    return JsonResponse(data,safe=False)


        