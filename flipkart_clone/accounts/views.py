from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError


def signup_view(request):
    
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            return redirect('login')
        except IntegrityError:
            error_message = "Username is already taken. Please choose a different one."
            return render(request, 'accounts/signup.html', {'error_message': error_message})
        return redirect('accounts/login.html')
    return render(request, 'accounts/signup.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('all_products')

        else:
            return render(request, 'accounts/login.html', {'error': 'Invalid Credentials'})
    return render(request, 'accounts/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')
