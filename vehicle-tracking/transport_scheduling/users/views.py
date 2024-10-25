from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import CustomUserCreationForm
from .models import CustomUser
from .decorators import admin_required

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Registration successful! Please log in.")
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')  # Redirect to a dashboard or homepage
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'registration/login.html')
def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully.")
    return redirect('login')
def admin_dashboard(request):
    # Add any necessary logic here
    return render(request, 'admin_dashboard.html')