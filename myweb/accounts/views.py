from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse 
from django.contrib.auth import login, authenticate,logout
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.decorators import login_required




def home(request):

    number=[1,2,3,4,5]
    name="ankush"
    args={'myname':name,'numbers':number}
    return render(request,'accounts/home.html',args)
@login_required
def register(request):
    if request.method=='POST':
        form= UserCreationForm(request.POST)
        if form.is_valid(): 
            form.save()
            return redirect('/accounts')
    else:
        form= UserCreationForm()
        args={'form':form}
        return render(request,'accounts/reg_form.html', args)        
def profile(request):
    args={'user':request.user}
    return render(request,"accounts/profile.html", args)


