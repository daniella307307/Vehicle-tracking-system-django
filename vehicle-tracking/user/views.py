from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm
from .models import Admin,Driver,Dispatcher,Customer

def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # Save the user to the User model
            user = form.save(commit=False)  # Don't save to the DB yet
            
            # Set the role based on the form input
            role = form.cleaned_data.get('role')
            user.role = role  # Assign the role to the user object
            
            # Save the user object to the correct model
            if role == 'admin':
                user.save()  # Save the User object
                Admin.objects.create(user=user)  # Create Admin instance
            elif role == 'driver':
                user.save()
                Driver.objects.create(user=user)  # Create Driver instance
            elif role == 'dispatcher':
                user.save()
                Dispatcher.objects.create(user=user)  # Create Dispatcher instance
            elif role == 'customer':
                user.save()
                Customer.objects.create(user=user)  # Create Customer instance
            
            # Log in the user
            login(request, user)  
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})
def home_view(request):
    return render(request, 'home.html')  
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
        
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('login') 