# Create your views here.
from django.shortcuts import render
import requests
from .models import City

def index(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=78949c9426f41a03ce87a45d00ac9fcc'
    
    cities = City.objects.all()
    
    weather_data = []
    
    for city in cities:
        city_weather = requests.get(url.format(city)).json()
        weather = {
            'city' : city.name,
            'temperature' : city_weather['main']['temp'],
            'description' : city_weather['weather'][0]['description'],
            'icon' : city_weather['weather'][0]['icon']
        }
        weather_data.append(weather)
    
    context = {'weather_data' : weather_data}
    return render(request, 'weather/index.html', context) #returns the index.html template
