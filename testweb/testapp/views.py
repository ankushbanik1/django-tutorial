from django.shortcuts import render, redirect,get_object_or_404
from  django.http import  HttpResponse
from  .models import Movie
from django.contrib.auth.forms import UserCreationForm
from django.template import loader
from django.contrib.auth import authenticate,login

def index(request):
    all_movie=Movie.objects.all()
   
    context={
       'all_movie': all_movie,
    }

    return render(request,'in.html',context)
def index1(request):
    return render(request,'in.html')
# Create your views here.
def details (request, movie_id):
    try:
        m1= Movie.objects.get(pk=movie_id)
    except Movie.DoesNotExist:
        raise Htt404(' ohh!! shitt!!!,this is wrong url !!!')
    return render(request,'index.html',{'m1':m1})

def login(request):
    return render(request,'login.html')    

def register(request):
    if request.method== "POST":


        
        form= UserCreationForm(request.POST)

        if form.is_valid():
           form.save()
           username=form.cleaned_data['username']
           password=form.cleaned_data['password1']
       
           user= authenticate(username=username, password=password)
           login(request,user)
           return redirect('index')
    else:
         form= UserCreationForm()
    context={'form': form}
    return render(request, 'register.html', context)

def profile(request):
    return HttpResponse("<h1>its your profile page</h1>")
def profile1(request,username='Default User'):
    return HttpResponse("<h1>its your profile page. your user name is :{}</h1>".format(username))    
