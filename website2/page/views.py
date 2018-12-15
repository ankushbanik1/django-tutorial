
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm,PasswordChangeForm
from django.contrib.auth import authenticate,login
from page.forms import editprofileForm
from django.contrib.auth.decorators import login_required


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


@login_required
def edit_profile(request):

    if request.method == 'POST':
        form = editprofileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect( 'profile')
    else:
        form = editprofileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'tem/edit_profile.html', args)


@login_required
def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect( 'profile')
        else:
                return redirect('change_password')
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'tem/change_password.html', args)        