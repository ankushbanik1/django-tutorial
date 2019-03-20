
from django.contrib import admin
from django.urls import path,include
from. import views
urlpatterns = [
    path('admin/', admin.site.urls),
path('page',include('page.urls',namespace='page')),
path('page',include('django.contrib.auth.urls')),

    # path('',views.home, name="home")
    path('',views.home.as_view(),name='home'),
    path('test/',views.test.as_view(),name='test'),
    path('thanks/',views.thanks.as_view(),name='thanks')
]
