from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from protisruti import settings
from django.core.mail import send_mail

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
        
        
        if User.objects.filter(username=username):
            messages.error(request, "Username already exists!")
            return redirect('home')
            
        if User.objects.filter(email=email):
            messages.error(request, "Email already registerd!")    
            return redirect('home')
        
        if len(username)>10:
            messages.error(request, "Username must be under 10 characters!")
            
        if pass1!= pass2:
            messages.error(request, "Passwords do not match!")
            
        
        if not username.isalnum():
            messages.error(request, "Username must be alphanumeric!")
            return redirect('home')    
            
                
            
        # Create user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()

        messages.success(request, "Your account has been created successfully. We have sent you a confirmation email, please confirm your email address in order to activate your account!")
        
        
        #welcome email......
        
        subject = "Welcome to Protisruti"
        message = "Hello " + myuser.first_name + "! \n" + "Welcome to Protisruti! \n Thank you for visiting our website. \n We have also sent you a confirmation email, please confirm your email address in order to activate your account. \nWe are glad to have you here. \n\n Thanking You! \n Team Protisruti"
        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=False)
        
        
        
        
        
        
        
        
        
        
        
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

