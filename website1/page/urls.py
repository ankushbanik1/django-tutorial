from django.http import HttpResponse
from django.conf.urls import url
from . import views
from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import views as auth_views
urlpatterns=[
    url(r'^$',views.home , name="home"),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^admin/logout/$', views.logout, name='logout'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    url(r'^changepassword/$', views.changepassword, name='changepassword'),
    

]