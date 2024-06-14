from django.urls import path
from . import views

urlpatterns = [
    path('api/catalog/getCategories', views.getCategorys),

]