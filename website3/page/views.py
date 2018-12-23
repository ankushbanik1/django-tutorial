from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
def home(request):
    return render(request,'tem/home.html')

def login(request):
    return render(request,'tem/login.html')
@login_required    
def about(request):
    return render(request,'tem/about.html')    


def register(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            user=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=authenticate(username='username',password='password')
            login(request,user)
            return redirect('home')

    else:
        form=UserCreationForm()
        args={'form':form} 
        return render(request,'tem/register.html',args)       




