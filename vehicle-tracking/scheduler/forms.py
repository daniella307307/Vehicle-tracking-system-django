from django import forms
from .models import Vehicle,Schedule

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['VIN', 'make', 'model', 'year', 'color', 'latitude', 'longitude']
        
    
class SchedulerForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['route_id', 'start_time', 'end_time']