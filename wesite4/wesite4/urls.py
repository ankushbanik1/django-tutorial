
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
urlpatterns = [
    path('admin/', admin.site.urls),
   url(r'^page/', include('page.urls')),

    path('', include('sendemail.urls')), # new
]
