from django.urls import path
from . import views

urlpatterns = [
    path('api/book/get_books', views.getBooks, name='getBooks'),
    path('api/book/get_detail/', views.getBookById),
    path('api/book/search/', views.searchBook),
    path('api/book/get_by_category/', views.getBookByCategory),
]