from django.urls import path
from .views import device_list, toggle_device

urlpatterns = [
    path('devices/', device_list, name='device_list'),
    path('toggle/<int:device_id>/', toggle_device, name='toggle_device'),
]