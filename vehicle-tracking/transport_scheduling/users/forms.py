from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    role = forms.ChoiceField(choices=CustomUser.ROLE_CHOICES, required=True)
    address = forms.CharField(max_length=200, required=False)
    phone_number = forms.CharField(max_length=15, required=False)
    driver_license = forms.CharField(max_length=20, required=False)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'address', 'phone_number', 'driver_license', 'password1', 'password2']
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.role = self.cleaned_data['role']
        user.address = self.cleaned_data['address']
        user.phone_number = self.cleaned_data['phone_number']
        user.driver_license = self.cleaned_data['driver_license']
        
        if commit:
            user.save()
        return user
