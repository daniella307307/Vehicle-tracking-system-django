from django.shortcuts import render, get_object_or_404, redirect
from .models import Vehicle
from .forms import VehicleForm, SchedulerForm
from user.models import Driver
from django.contrib.auth.decorators import login_required
# List all vehicles
@login_required
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
            vehicle = form.save(commit=False)
            # Assign a driver if specified in the form (ensure you have a way to select a driver)
            driver_id = request.POST.get('driver')  # Assuming you have a driver field in the form
            if driver_id:
                vehicle.driver = Driver.objects.get(id=driver_id)
            vehicle.save()
            return redirect('vehicle_list')  # Redirect to the list view after saving
    else:
        form = VehicleForm(instance=vehicle)

    return render(request, 'vehicles/vehicle_form.html', {'form': form})
# Vehicle location view
def vehicle_location(request, pk):
    vehicle = get_object_or_404(Vehicle, pk=pk)
    return render(request, 'vehicles/vehicle_location.html', {'vehicle': vehicle})

def create_schedule(request, vehicle):
    if pk:
        vehicle = get_object_or_404(Vehicle, pk=pk)
        if request.method == 'POST':
            # Process the schedule form data
            schedule_form = SchedulerForm(request.POST)
            if schedule_form.is_valid():
                # Save the schedule
                schedule = schedule_form.save(commit=False)
                schedule.vehicle = vehicle
                schedule.save()
                return redirect('vehicle_location', pk=vehicle.pk)
        else:
            schedule_form = SchedulerForm()