
from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from testapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/',views.emp_data),
    path('api/json/',views.emp_data_json),
    path('api/json2/',views.emp_data_json2),
    path('api/jsoncbv/',views.jsonCBV.as_view()),
    path('api/employee/',views.emplyeeditails.as_view()),
    url(r'^api/$',views.emplyeelist.as_view()),
]
