from django import forms
from .models import Vehicle, Driver, Schedule, Route

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['VIN', 'make', 'model', 'year', 'color', 'latitude', 'longitude', 'driver']
        widgets = {
            'VIN': forms.TextInput(attrs={'class': 'form-control'}),
            'make': forms.TextInput(attrs={'class': 'form-control'}),
            'model': forms.TextInput(attrs={'class': 'form-control'}),
            'year': forms.NumberInput(attrs={'class': 'form-control'}),
            'color': forms.TextInput(attrs={'class': 'form-control'}),
            'capacity': forms.NumberInput(attrs={'class': 'form-control'}),
            'latitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'longitude': forms.NumberInput(attrs={'class': 'form-control', 'step': 'any'}),
            'driver': forms.Select(attrs={'class': 'form-control'}),
        }

class DriverForm(forms.ModelForm):
    class Meta:
        model = Driver
        fields = ['name', 'license_number', 'contact_number']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'license_number': forms.TextInput(attrs={'class': 'form-control'}),
            'contact_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['start_location', 'end_location', 'distance', 'duration']
        widgets = {
            'start_location': forms.TextInput(attrs={'class': 'form-control'}),
            'end_location': forms.TextInput(attrs={'class': 'form-control'}),
            'distance': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration': forms.NumberInput(attrs={'class': 'form-control'}),
        }

class ScheduleForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['vehicle', 'driver', 'route', 'departure_time', 'arrival_time']
        widgets = {
            'vehicle': forms.Select(attrs={'class': 'form-control'}),
            'driver': forms.Select(attrs={'class': 'form-control'}),
            'route': forms.Select(attrs={'class': 'form-control'}),
            'departure_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'arrival_time': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
