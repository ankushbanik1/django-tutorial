from django.contrib import admin
from  django.conf.urls import  url
from . import views
urlpatterns=[
    url(r'^$', views.index,name="index"),
    url(r'^(?P<movie_id>[0-9]+)/$',views.details, name='details'),
]