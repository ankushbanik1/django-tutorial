from django.http import HttpResponse
from django.template import loader

from django.shortcuts import render
from django.http import Http404
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
from .forms import UserForm
from .models import Album

def index(request):
   
    return render(request,'in.html')
def details(request):
    
    return render(request, 'music/details.html' ) 
class UserFormView(View):
     form_class = UserForm
     template_name='music/registration.html'




#display blank form
     def get(self,request):
         form=self.form_class(None)
         return render(request,self.template_name,{'form':form})
     def post(self,request):
         form=self.form_class(request.POST)
         if form.is_valid():
             user= form.save(commit=False)
             #cleaned (normalize) data
             username= form.cleaned_data['username']
             password= form.cleaned_data['password']
             user.set_password(password)
             user.save()

             user= authenticate(username=username, password=password)
             if user is not None:
                 if user.is_active:
                     login(request,user)
                     return redirect('index')
         return render(request,self.template_name,{'form':form})
