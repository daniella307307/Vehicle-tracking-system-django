from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .models import Vehicle, Driver, Schedule, Route
from .forms import VehicleForm, DriverForm, ScheduleForm, RouteForm
from django.contrib.auth.decorators import login_required


# Vehicle Views

@login_required
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    vehicle_names = [vehicle.make for vehicle in vehicles]
    vehicle_data = [vehicle.capacity for vehicle in vehicles]  
    
   

    return render(request, 'transport/vehicle_list.html', {'vehicles': vehicles, 'vehicle_name':vehicle_names, 'vehicle_data':vehicle_data})
def vehicle_data(request):
    vehicles = Vehicle.objects.all()
    
    # Prepare data for JSON response
    vehicle_data = [
        {
            "name": vehicle.make,
            "capacity": vehicle.capacity
        }
        for vehicle in vehicles
    ]
    
    # Return data as JSON
    return JsonResponse({"vehicles": vehicle_data}, safe=False)
@login_required
def add_vehicle(request):
    if request.method == 'POST':
        form = VehicleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transport:dashboard')
    else:
        form = VehicleForm()
    return render(request, 'transport/add_vehicle.html', {'form': form})

@login_required
def edit_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    if request.method == 'POST':
        form = VehicleForm(request.POST, instance=vehicle)
        if form.is_valid():
            form.save()
            return redirect('transport:dahsboard')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'transport/edit_vehicle.html', {'form': form, 'vehicle': vehicle})

@login_required
def delete_vehicle(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    vehicle.delete()
    return redirect('transport:dashboard')

# Driver Views
@login_required
def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'transport/driver_list.html', {'drivers': drivers})

@login_required
def add_driver(request):
    if request.method == 'POST':
        form = DriverForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transport:dashboard')
    else:
        form = DriverForm()
    return render(request, 'transport/add_driver.html', {'form': form})

@login_required
def edit_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    if request.method == 'POST':
        form = DriverForm(request.POST, instance=driver)
        if form.is_valid():
            form.save()
            return redirect('transport:dashboard')
    else:
        form = DriverForm(instance=driver)
    return render(request, 'transport/edit_driver.html', {'form': form, 'driver': driver})

@login_required
def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    driver.delete()
    return redirect('transport:dashboard')

# Route Views
@login_required
def route_list(request):
    routes = Route.objects.all()
    return render(request, 'transport/route_list.html', {'routes': routes})

@login_required
def add_route(request):
    if request.method == 'POST':
        form = RouteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transport:dashboard')
    else:
        form = RouteForm()
    return render(request, 'transport/add_route.html', {'form': form})

@login_required
def edit_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    if request.method == 'POST':
        form = RouteForm(request.POST, instance=route)
        if form.is_valid():
            form.save()
            return redirect('transport:dashboard')
    else:
        form = RouteForm(instance=route)
    return render(request, 'transport/edit_route.html', {'form': form, 'route': route})

@login_required
def delete_route(request, route_id):
    route = get_object_or_404(Route, id=route_id)
    route.delete()
    return redirect('transport:dashboard')

# Schedule Views

@login_required
def schedule_list(request):
    schedules = Schedule.objects.all()
    return render(request, 'transport/schedule_list.html', {'schedules': schedules})
@login_required
def add_schedule(request):
    if request.method == 'POST':
        form = ScheduleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transport:dashboard')
    else:
        form = ScheduleForm()
    return render(request, 'transport/add_schedule.html', {'form': form})
@login_required
def edit_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    if request.method == 'POST':
        form = ScheduleForm(request.POST, instance=schedule)
        if form.is_valid():
            form.save()
            return redirect('transport:dashboard')
    else:
        form = ScheduleForm(instance=schedule)
    return render(request, 'transport/edit_schedule.html', {'form': form, 'schedule': schedule})
@login_required
def delete_schedule(request, schedule_id):
    schedule = get_object_or_404(Schedule, id=schedule_id)
    schedule.delete()
    return redirect('transport:dashboard')

@login_required
def driver_vehicle_route_list(request):
  
    driver_data = Driver.objects.all().select_related('vehicle', 'route')  
    
    return render(request, 'transport/dashboard.html', {'driver_data': driver_data})
@login_required
def dashboard(request):
    user = request.user

    drivers = Driver.objects.all()
    routes = Route.objects.all()
    vehicles = Vehicle.objects.all()
    schedules=Schedule.objects.all()
    try:
       
        role = user.role
        
    except Exception as e:
        role ='NO Role Assigned'
        
    return render(request, 'transport/dashboard.html', {
        'role': role,
        'user':user,
        'schedules':schedules,
        'drivers': drivers,
        'routes': routes,
        'vehicles': vehicles,
        })