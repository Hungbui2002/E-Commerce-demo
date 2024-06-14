from django.urls import path
from . import views

urlpatterns = [
    path('api/shipment/get-shipments', views.list_shipments),
]