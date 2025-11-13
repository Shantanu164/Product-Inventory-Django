from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse

def home(request):
    return render(request, 'ProdInvApp/home.html')

def index(request):
    return render(request, 'ProdInvApp/index.html')
