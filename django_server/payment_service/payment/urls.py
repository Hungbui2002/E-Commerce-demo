from django.urls import path
from . import views

urlpatterns = [
    path('api/payment/get-payments', views.list_payments),
]