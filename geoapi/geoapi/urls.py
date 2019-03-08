

from django.contrib import admin
from django.urls import path
from page import views
from .import views
urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/', views.home, name='home'),
]