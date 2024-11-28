# accounts/views.py
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import HttpResponse

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_confirm = request.POST.get('password_confirm')

        # Basic validation
        if not username or not email or not password or not password_confirm:
            messages.error(request, "All fields are required.")
            return redirect('signup')

        if password != password_confirm:
            messages.error(request, "Passwords do not match.")
            return redirect('signup')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken.")
            return redirect('signup')

        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
            return redirect('signup')

        # Create the user
        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)  # Log the user in immediately after signup
        messages.success(request, "Account created successfully!")
        return redirect('home')  # Redirect to a home page (adjust as needed)

    return render(request, 'accounts/signup.html')
