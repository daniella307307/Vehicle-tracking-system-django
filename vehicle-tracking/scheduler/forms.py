from django import forms
from .models import Vehicle,Schedule
from user.models import Driver

class VehicleForm(forms.ModelForm):
    driver = forms.ModelChoiceField(queryset=Driver.objects.all(), required=False)  
    
    class Meta:
        model = Vehicle
        fields = ['VIN', 'make', 'model', 'year', 'color', 'latitude', 'longitude', 'driver']
    
class SchedulerForm(forms.ModelForm):
    class Meta:
        model = Schedule
        fields = ['route_id', 'start_time', 'end_time']