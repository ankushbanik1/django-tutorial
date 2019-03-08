from django.urls import path
from django.conf.urls import url,include
from.import views
from django.contrib.auth import views as auth_view


urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/',auth_view.LoginView.as_view(template_name='tem/login.html'),name='login'),
    url(r'^logout/',auth_view.LogoutView.as_view(template_name='tem/home.html'),name='logout'),
    url(r'^register/', views.register, name="register"),
    url(r'^about/', views.about, name="about"),
    url(r'^edit_profile/', views.edit_profile, name="edit_profile"),
    url(r'^change_password/', views.change_password, name="change_password"),
 
]
