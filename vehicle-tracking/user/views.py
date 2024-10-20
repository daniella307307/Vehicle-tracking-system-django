from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm
# Create your views here.
def register_user(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Save the user
            login(request)  # Log the user in after successful registration
            return redirect('home.html')  # Redirect to home page after login
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'register.html', {'form': form})

def home_view(request):
    return render(request, 'home.html')  # Render home page
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