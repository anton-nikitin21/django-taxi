from django.urls import path
from .views import (
    home,
    car_list,
    driver_list,
    order_list,
    car_detail,
    driver_detail,
    order_detail,
)

urlpatterns = [
    path('', home, name='home'),
    path('cars/', car_list, name='car_list'),
    path('drivers/', driver_list, name='driver_list'),
    path('orders/', order_list, name='order_list'),

    path('cars/<int:pk>/', car_detail, name='car_detail'),
    path('drivers/<int:pk>/', driver_detail, name='driver_detail'),
    path('orders/<int:pk>/', order_detail, name='order_detail'),
]