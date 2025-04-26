from django.shortcuts import render
from django.http import HttpResponse as HttpsResponse

# Create your views here.


def home(request):
    return HttpsResponse("hello home page")
