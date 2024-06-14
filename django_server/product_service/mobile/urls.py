from django.urls import path
from . import views

urlpatterns = [
    path('api/mobile/get_mobiles', views.getMobile, name='getMobiles'),
    path('api/mobile/get_detail/', views.getMobileById),
    path('api/mobile/search', views.searchMobile),
    path('api/mobile/get_by_category/', views.getClothesByCategory),
]