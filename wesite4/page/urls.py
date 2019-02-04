
from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url
from page.views import *
from rest_framework import routers
from . import views
# router=routers.DefaultRouter()
# router.register("",pageViewSet)


# urlpatterns = [
#   path('page/',include(router.urls)),
# ]
urlpatterns=[
  path('home/',views.home,name="homepage"),
  path('reg/',views.register,name="reg")
]