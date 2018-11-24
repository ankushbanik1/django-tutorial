from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,"tem1/home.html")

def contact(request):
    return render(request,'tem1/contact.html')   
    
     