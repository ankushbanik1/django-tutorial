from django.shortcuts import render
from django.http import HttpResponse 
from django.contrib.auth import login, authenticate,login
# Create your views here.
def home(request):

    number=[1,2,3,4,5]
    name="ankush"
    args={'myname':name,'numbers':number}
    return render(request,'accounts/login.html',args)
