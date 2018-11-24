from django.shortcuts import render
from . import views
from django.http import HttpResponse
def home1(request):
    return render(request,"tem1/home.html")
