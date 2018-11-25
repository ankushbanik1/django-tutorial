from django.contrib import admin
from music import views

from django.conf.urls import include,url

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^music/', include("music.url")),
  
   
]


