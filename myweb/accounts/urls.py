from django.conf.urls import url 
from. import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    url(r'^$', views.home),
    

    url( r'^login/$',auth_views.LoginView.as_view(template_name="accounts/login.html"), name="login"),

    url( r'^logout/$',auth_views.LogoutView.as_view(template_name="accounts/logout.html"), name="logout"),
    url(r'^register/$', views.register, name='register'),
    url(r'^home/$', views.home, name='home'),
    url(r'^profile/$', views.profile, name='profile')

]