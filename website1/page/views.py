from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm


def home(request):
    return render(request,"tem1/home.html")

def contact(request):
    return render(request,'tem1/contact.html')   
    
def login(request):
    return render(request,'tem1/login.html')     
def register(request):
    if  request.method=='POST':

        form=UserCreationForm(request.POST)
        if form.is_valid():
           form.save()
           user=form.cleaned_data['username']
           password=form.cleaned_data['password']
           

           user=authenticate(username=username, password=password)
           login(request,user)
           return redirect('home')

    else:
        form=UserCreationForm()
        context={
            'form':form
        }
        return render(request,'tem1/register.html',context)     

           


