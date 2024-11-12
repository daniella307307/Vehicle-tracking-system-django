from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import UserRegistrationForm, UserLoginForm, ProfileForm
from .models import Profile

def register_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        profile_form = ProfileForm(request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user instance
            user = user_form.save()

            # Create and save the profile instance with the role
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            messages.success(request, 'Registration successful.')
            return redirect('login_user')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        user_form = UserRegistrationForm()
        profile_form = ProfileForm()

    return render(request, 'users/registration.html', {
        'user_form': user_form,
        'profile_form': profile_form,
    })

def login_user(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('transport:dashboard')  # Redirect to dashboard after login
            else:
                messages.error(request, 'Invalid username or password.')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})

@login_required
def logout_user(request):
    logout(request)
    return redirect('login_user')

@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile updated successfully.')
            return redirect('transport:dashboard')
    else:
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'users/edit_profile.html', {'profile_form': profile_form})
