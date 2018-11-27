
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views as views1
from page import views 
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainView, TokenRefreshView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views1.home1),
   
    url(r'^page/', include('page.urls')),
    url(r'^language/',views.language.as_view()), 
    url(r'^programmer/',views.programmer.as_view()),

    url(r'^paradigm/',views.paradigm.as_view()),
    
     
    url(r'^api/token/$', TokenObtainView.as_view()),

    url(r'^api/token/refresh/$',TokenRefreshView.as_view()),





]
urlpatterns=format_suffix_patterns(urlpatterns)