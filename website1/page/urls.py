from django.http import HttpResponse
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

urlpatterns=[
    url(r'^$',views.home , name="home"),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    
   
]

