import requests

api_address =" http://api.openweathermap.org/data/2.5/weather?appid=cbce7a800907c7ef1cd00bea2092bd01&q= "
city= input('city name:')

url =api_address+city

json_data= requests.get(url).json()


print(json_data)