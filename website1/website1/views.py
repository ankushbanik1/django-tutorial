from django.shortcuts import render
from . import views
from django.http import HttpResponse
from django.core.mail import send_mail


def home1(request):
    return render(request,"tem1/home.html")

def send(request):
    send_mail('HELLO FROM ANKUSH',
    'HELLO THERE ITS A AUTOMETED MASSAGE',
    'ankushabanik123@gmail.com',['dofidiyec@daabox.com'],
    fail_silently=False)
    return render(request, 'tem1/send.html')    
