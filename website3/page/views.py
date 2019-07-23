from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,PasswordChangeForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth.decorators import login_required
from page.forms import ContactForm
def home(request):
    return render(request,'tem/home.html')

def login(request):
    return render(request,'tem/login.html')
@login_required    
def about(request):
    return render(request,'tem/about.html')    


# def register(request):
def register(request):
    if request.method=='POST':

        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']

            user=authenticate(username=username,password=password)
            login(request,user)
            return redirect('page')

    else:
        form=UserCreationForm()
        args={'form':form}
        return render(request,'tem/register.html',args) 


# def edit_profile (request):

#     if request.method=='POST':

#         form=editprofile_form(request.POST,instance=request.user)
#         if form.is_valid():
#             form.save()
#             return redirect('login')

#     else:
#         form=editprofile_form(instance=request.user)
#         args={'form':form}
#         return render(request,'tem/edit_form.html',args)    
@login_required    
    
def edit_profile(request):

    if request.method == 'POST':
        form = editprofileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect( 'login')
    else:
        form = editprofileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'tem/edit_form.html', args)


@login_required    

def profile(request):
       return render(request,'tem/profile.html')




def change_password(request):

    if request.method == 'POST':
        form = PasswordChangeForm(request.POST,user=request.user)

        if form.is_valid():
            form.save()
            return redirect( '/accounts/profile')
        else:
            return redirect('/page/change_password')        
            
    else:
        form = PasswordChangeForm(user=request.user)
        args = {'form': form}
        return render(request, 'tem/change_password.html', args)


# email contact us.................................................


from django.core.mail import send_mail, BadHeaderError

def send_email(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        send_mail('Subject goes here', 'Message goes here', 'no-reply@authapplciation.com', [email], fail_silently=False)
        return HttpResponse("Mail Sent to " + email)

    return render(request, 'tem/contact.html')