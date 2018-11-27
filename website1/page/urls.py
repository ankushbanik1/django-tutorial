from django.http import HttpResponse
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm

urlpatterns=[
    url(r'^$',views.home , name="home"),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^register/$', views.register, name='register'),
    
   
]

