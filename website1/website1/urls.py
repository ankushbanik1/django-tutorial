
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home1),
    url(r'^page/', include('page.urls'))
]
