from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle
from .forms import VehicleForm

# List all vehicles
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})

# Create or update a vehicle
def vehicle_create_or_update(request, pk=None):
    if pk:
        vehicle = get_object_or_404(Vehicle, pk=pk)
    else:
        vehicle = Vehicle()  # Create a new vehicle instance if no pk is provided

    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('vehicle_list')  # Redirect to the list view after saving
    else:
        form = VehicleForm(instance=vehicle)

    return render(request, 'vehicles/vehicle_form.html', {'form': form})

# Vehicle location view
def vehicle_location(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicles/vehicle_location.html', {'vehicle': vehicle})
