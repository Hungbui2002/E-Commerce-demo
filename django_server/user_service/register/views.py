from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from .forms import *
import logging
from django.views.decorators.http import require_http_methods
import json

# Tạo một logger instance
logger = logging.getLogger(__name__)


@csrf_exempt
@require_http_methods(["POST"])
def register(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        username = data['username']
        isExist = User.objects.filter(username=username)
        if isExist.exists():
            return JsonResponse({'status': 2, 'message': 'User has exit!'})
        user_form = UserRegistrationForm(data)
        customer_form = CustomerRegistrationForm(data)
        
        if user_form.is_valid() and customer_form.is_valid():
            # Lưu thông tin của User
            user = user_form.save(commit=False)
            user.set_password(user_form.cleaned_data['password'])
            user.save()
            # Lưu thông tin của Customer
            customer = customer_form.save(commit=False)
            customer.user = user
            customer.save()

            return JsonResponse({'status': 1, 'message': 'User registered successfully'})
        else:
            return JsonResponse({'status': 0, 'message': 'Invalid form data'}, status=400)
        