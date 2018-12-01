from django.urls import path
from. import views as v


urlpatterns=[
    path('weather/',v.index, name='index'),
]