from django.contrib import admin
from django.conf.urls import  url
from . import views
urlpatterns=[
    #/music/
    
    url(r'^$', views.index, name='index'),
   # url(r'^register/$', views.UserFormView.as_view(), name='register'),

    url(r'^details/$',views.details, name='details'),
   

      #/music/712/

]