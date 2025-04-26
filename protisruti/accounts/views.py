from django.shortcuts import render,redirect
from django.http import HttpResponse 


# Create your views here.


def home(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')

def login_view(request):
    return render(request, 'login.html')

def logout_view(request):
    pass