from django.urls import path
from . import views

urlpatterns = [
    path('api/user/infor',views.getCustomer),
]