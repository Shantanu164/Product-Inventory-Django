from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

def home(request):
    return HttpResponse("Product Inventory Management System.Home Page.")

def index(request):
    return HttpResponse("Product Inventory Management System.Index Page.")