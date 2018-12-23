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
    url(r'^login/',auth_views.LoginView.as_view(template_name='tem1/login.html'),name='login'),
      url(r'^logout/',auth_views.LogoutView.as_view(template_name='tem1/logout.html'),name='logout'),
    url(r'^admin/logout/$', views.logout, name='logout'),
    url(r'^profile/edit/$', views.edit_profile, name='edit_profile'),
    
    url(r'^changepassword/$', views.changepassword, name='changepassword'),
    

]