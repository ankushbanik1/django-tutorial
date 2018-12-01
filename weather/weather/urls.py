
from django.contrib import admin
from django.urls import path,include
from django.conf import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('climate.urls'))
]
