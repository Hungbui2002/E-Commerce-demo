from django.urls import path
from . import views

urlpatterns = [
    path('api/search/searh_by_key/',views.search_product_by_key,name='search_by_key'),
    # path('search_by_image',views.search_product_by_image,name='search_by_image'),
    # path('search_by_voice/', views.vocie_search, name='search_by_voice'),
    # path('api/search/key_search', views.vocie_search, name='search_by_voice'),
]