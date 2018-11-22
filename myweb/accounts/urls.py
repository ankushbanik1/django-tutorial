from django.conf.urls import url 
from. import views
from django.contrib.auth import views as auth_views
urlpatterns=[
    url(r'^$', views.home),
       url( r'^login/$',auth_views.LoginView.as_view(template_name="accounts/home1.html"), name="login1"),


]