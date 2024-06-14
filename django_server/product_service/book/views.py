from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from django.http import JsonResponse
from .models import Book
from product_service.utils import serializer
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
@require_http_methods(["GET"])
def getBooks(request):
    books = Book.objects.all()
    data = serializer(books)
    return JsonResponse(data,safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def getBookById(request):
    data = {}
    try:
        book_id = request.GET.get('product_id')
        book = Book.objects.get(product_id=book_id)
        data = book.to_json()
    except:
        pass
    return JsonResponse(data,safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def searchBook(request):
    key = request.GET.get('key')
    category_id = request.GET.get('category_id')
    data = []
    try:
        books = Book.objects.filter(name__icontains=key, category_id=category_id)
        data = serializer(books)
    except:
        pass
    return JsonResponse(data,safe=False)

@csrf_exempt
@require_http_methods(["GET"])
def getBookByCategory(request):
    category_id = request.GET.get('category_id')
    data = []
    try:
        books = Book.objects.filter(category_id=category_id)
        data = serializer(books)
    except:
        pass
    return JsonResponse(data,safe=False)

