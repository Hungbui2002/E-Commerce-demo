from django.urls import path
from . import views

urlpatterns = [
    path('api/clothes/get_clothes', views.getclothes, name='getClothes'),
    path('api/clothes/get_detail/', views.getClotheById),
    path('api/clothes/search/', views.searchClothes),
    path('api/clothes/get_by_category/', views.getClothesByCategory),
]