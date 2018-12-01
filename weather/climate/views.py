from django.shortcuts import render

import requests


def index(request):
    url='http://api.openweathermap.org/data/2.5/weather?appid=cbce7a800907c7ef1cd00bea2092bd01&q=kolkata '
    
    r= requests.get(url.(city).json()
    city_weather={
        
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],

   }
    context={ 'city_weather':city_weather}
    return render(request,'weather.html',context)
# Create your views here.
