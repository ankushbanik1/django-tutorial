from django.contrib import admin
from music import views
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include,url
from company import views

urlpatterns = [
   url(r'^admin/', admin.site.urls),
   url(r'^music/', include("music.url")),
   url(r'^stocks/',views.stocklist.as_view()),

  
   
]
urlpatterns = format_suffix_patterns(urlpatterns)


