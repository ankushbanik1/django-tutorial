from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    path('',views.shop,name="shop"),
    path('about/',views.about,name="about"),
    path('contact/',views.contact,name="contact"),
    path('traking/',views.traking,name="traking"),
    path('productview/',views.productview,name="productview"),
    path('checkout/',views.checkout,name="checkout"),
    path('search/',views.search,name="search"),
    
]
