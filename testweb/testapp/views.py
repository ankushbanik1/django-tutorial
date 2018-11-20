from django.shortcuts import render
from  django.http import  HttpResponse
from  .models import Movie

from django.template import loader

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