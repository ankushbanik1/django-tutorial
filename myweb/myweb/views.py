from django.shortcuts import redirect
from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.forms import UserCreationForm

def login_redirect(request):
    return redirect('/accounts/login')
    
def home1(request):

    
    return render(request,'accounts/home.html')    
