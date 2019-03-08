
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from page import views as vi

urlpatterns = [
    path('admin/', admin.site.urls),
    url(r'^page/',include('page.urls')),
    url(r'^accounts/profile/', vi.profile, name="profile"),
]
