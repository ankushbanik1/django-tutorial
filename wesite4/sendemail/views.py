from django.shortcuts import render

# Create your views here.
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import ContactForm
def emailView(request):

    if request.method == 'GET':


        form = EmailForm()
    else:


        form = EmailForm(request.POST)
if form.is_valid():

   cd = form.cleaned_data
subject = 'Your subject goes here'
message = 'The Mail is from {}... The Message is {} .. Email is {}'.format(cd['Name'], cd['Message'], cd['Email'])
Email = '{}'.format(cd['Email'])
try:
send_mail(subject, message , Email, ['admin@gmail.com'])
except BadHeaderError:
return HttpResponse('Email did not send')
return render(request, "email/success.html") # 
return render(request, "email/mail.html", {'form': form})

# if you want to add more fields into just one.. increas the tuple curly-brackets vice-versa