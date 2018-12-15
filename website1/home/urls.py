from django.conf.urls import url
from home.views import homeview


urlpatterns=[
    url(r'^$',homeview.as_view(),name='homeview')
    
]