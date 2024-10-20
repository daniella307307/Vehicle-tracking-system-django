from django.urls import path
from .views import vehicle_list, vehicle_create, vehicle_update

urlpatterns = [
    path('vehicles/', vehicle_list, name='vehicle_list'),
    path('vehicles/create/', vehicle_create, name='vehicle_create'),
    path('vehicles/<int:pk>/update/', vehicle_update, name='vehicle_update'),
]
