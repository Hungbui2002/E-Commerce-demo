from django.urls import path
from . import views

urlpatterns = [
    path('api/user/login',views.login),
]