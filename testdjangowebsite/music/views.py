from django.http import HttpResponse
from . models import Album


def index(request):
    all_albums= Album.objects.all()
    html=''
    for album in all_albums:
        url= '/music/' + str(album.id)+ '/'
        html +='<a herf="'+ url +'">'+ album.album_title+"</a><br>"
    return HttpResponse(html)
def details(request,album_id):
    return HttpResponse("<h2> ditais for album id:" +str(album_id)+"</h2>" )