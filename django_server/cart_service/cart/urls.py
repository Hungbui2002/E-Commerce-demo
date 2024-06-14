from django.urls import path
from . import views

urlpatterns = [
    path('api/cart/delete/<int:cart_id>', views.remove_item, name='delete_cart_item'),
    path('api/cart/save',views.save_item,name="save_item"),
    path('api/cart/getCarts',views.get_cart_items,name="items_cart"),
    path('api/cart/add_to_cart',views.add_to_cart,name='add_to_cart'),
]