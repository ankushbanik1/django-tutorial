
from django.urls import path,include
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

app_name='page'
urlpatterns =[
    url(r'login/$',auth_views.LoginView.as_view(template_name="page/login.html"),
    name='login'),
     url(r'logout/$',auth_views.LogoutView.as_view(),
    name='logout'),
     url(r'signup/$',views.SignUp.as_view(),
    name='signup')
       
]