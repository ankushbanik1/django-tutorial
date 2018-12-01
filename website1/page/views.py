from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm,UserChangeForm
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,permissions
from .models import Language,Paradigm,Programmer
from django.contrib.auth.models import User
from .serializer import Languageserializer,Paradigmserializer ,Programmerserializer
from django.urls import reverse

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



class language(APIView):

    def get(self,request):
        language=Language.objects.all()
        serializer= Languageserializer(language,many=True)
        permission_classes=(permissions.IsAuthenticatedOrReadOnly,)
        return Response (serializer.data)
        pass


    

class paradigm(APIView):


    def get(self,request):
        paradigm=Paradigm.objects.all()
        serializer= Paradigmserializer(paradigm,many=True)
        return Response (serializer.data)
        pass
    
class programmer(APIView):


    def get(self,request):
        programmer=Programmer.objects.all()
        serializer= Programmerserializer(programmer,many=True)
        return Response (serializer.data)
        pass
    def post(self):
        pass
def profile(request):
    args={'user':request.user}
    return render (request,'tem1/profile.html')  

# def edit_profile(request):
#     if request.method=='POST':
#         form=UserChangeForm(request.POST,instance=request.user)
#         if form.is_valid():

#             form.save()

#             return redirect(reverse('accounts:view_profile'))
#         else:
#             form= UserChangeForm(instance=request.user)
#             args= {'form':form }
#             return render(request,'tem1/edit_profile.html',args)
def edit_profile(request):
    if request.method == 'POST':
        form = UserChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect( '/page/profile')
    else:
        form = UserChangeForm(instance=request.user)
        args = {'form': form}
        return render(request, 'tem1/edit_profile.html', args)