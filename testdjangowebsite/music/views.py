from django.http import HttpResponse
from django.template import loader
from .models import Album
from django.shortcuts import render

def index(request):
    all_albums= Album.objects.all()
    
    context={
        'all_albums': all_albums,
    }
    
    return render(request,'in.html', context)
def details(request,album_id):
    return HttpResponse("<h2> ditais for album id:" +str(album_id)+"</h2>" )