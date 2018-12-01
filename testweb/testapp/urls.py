from django.contrib import admin
from  django.conf.urls import  url
from . import views
from django.urls import path


urlpatterns=[
    url(r'^$', views.index,name="index"),
    url(r'^(?P<movie_id>[0-9]+)/$',views.details, name='details'),
    
    url(r'^login/$',views.login,name="login"),
    url(r'^register/$',views.register,name="register"),
    path('profile/<username>/',views.profile1,name="profile"),
    path('profile/', views.profile),
   

    




]