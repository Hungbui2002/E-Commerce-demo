from django.urls import path
from . import views

urlpatterns = [
    path('api/order/create-order', views.create_order),
    path('api/order/update-order', views.update_order),
    path('api/order/delete/<int:order_id>', views.delete_order),
    path('api/order/getVouchers', views.list_voucher),
]