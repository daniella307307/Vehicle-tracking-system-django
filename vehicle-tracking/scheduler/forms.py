from django import forms
from .models import Vehicle

class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = ['VIN', 'make', 'model', 'year', 'color', 'latitude', 'longitude']