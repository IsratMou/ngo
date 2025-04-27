from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        pass1 = request.POST.get('pass1')
        pass2 = request.POST.get('pass2')

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(
            request, "Your account has been created successfully!")
        return redirect('login')

    # If not POST method, render the signup page
    return render(request, 'signup.html')


def login_view(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass1')

        # Authenticate user
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            messages.success(request, "You are logged in successfully!")

            fname = user.first_name

            return redirect('home')
        else:
            messages.error(request, "Invalid credentials!")
            return redirect('home')

    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, "You are logged out successfully!")
    return redirect('home')

