from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate,login

from django.contrib.auth.decorators import login_required

# Create your views here.
# from rest_framework import viewsets
# from django.contrib.auth.models import User

# from page.serializer import pageSerializer
# class Pagesirializer(viewsets.ModelViewSet):
#     queryset=User.objects.all()
#     serializer_class=pageSerializer
def home(request):
    return render(request,"tem/hompage.html")


def register(request):
        if request.method=="POST":
            forms=UserCreationForm(request.POST)
            if forms.is_valid():

                forms.save()
                username=forms.cleaned_data['user_name']
                password=forms.cleaned_data['password']
                user=authenticate(username=username,password=password)
                login(user,request)
                return redirect("/page/home")
        else:
            forms=UserCreationForm()
            args={"forms":forms}

            return render(request,"tem/register.html",args)
                