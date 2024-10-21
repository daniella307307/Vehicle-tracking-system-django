from django.urls import path
from .views import vehicle_location,vehicle_create_or_update,vehicle_list

urlpatterns = [
    path('vehicles/', vehicle_list, name='vehicle_list'),
    path('vehicle/create/', vehicle_create_or_update, name='vehicle_create'),
    path('vehicle/<int:pk>/update/', vehicle_create_or_update, name='vehicle_update'),
    path('vehicle/<int:pk>/location/', vehicle_location, name='vehicle_location'),
]