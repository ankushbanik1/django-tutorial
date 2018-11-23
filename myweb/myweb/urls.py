from django.conf.urls import url, include
from django.contrib import admin
from myweb import views as myweb_views
urlpatterns = [
    url(r'^$', myweb_views.login_redirect, name='login_redirect'),
    url(r'^admin/', admin.site.urls),
    url(r'^home/$',myweb_views.home1),
    url(r'^accounts/', include('accounts.urls'))
    
   
]