
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate,login


def register(request):
    if request.method=='POST':

        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['user_name']
            password=form.cleaned_data['password']

            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('/')

    else:
        form=UserCreationForm()
        args={'form':form}
        return render(request,'tem/register.html',args)      
def profile(request):
    args={"user " : request.user}
    return render(request,'tem/profile.html',args)
