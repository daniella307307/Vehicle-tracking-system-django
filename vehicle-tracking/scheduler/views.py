from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle, Driver, Route, Location, Scheduler

# List all vehicles
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})

# Create a new vehicle
def vehicle_create(request):
    if request.method == "POST":
        # Handle the form submission
        # Add code to create a Vehicle instance here
        return redirect('vehicle_list')
    return render(request, 'vehicles/vehicle_form.html')

# Update vehicle
def vehicle_update(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    if request.method == "POST":
        # Handle the form submission
        # Add code to update the Vehicle instance here
        return redirect('vehicle_list')
    return render(request, 'vehicles/vehicle_form.html', {'vehicle': vehicle})
