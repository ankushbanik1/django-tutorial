
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views as views1
from page import views 
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework_simplejwt.views import TokenObtainView, TokenRefreshView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views1.home1),
    url(r'home/', include('home.urls')),
    url(r'^page/', include('page.urls')),
    url(r'^language/',views.language.as_view()), 
    url(r'^programmer/',views.programmer.as_view()),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    url(r'^accounts/profile/(?P<pk>\d+)/$', views.profile, name='profile_vk'),
    url(r'^paradigm/',views.paradigm.as_view()),
    
     
    url(r'^api/token/$', TokenObtainView.as_view()),
    path('sendmail/',views1.send),

    url(r'^api/token/refresh/$',TokenRefreshView.as_view()),
    path('api-auth/',include('rest_framework.urls'))






]
urlpatterns=format_suffix_patterns(urlpatterns)