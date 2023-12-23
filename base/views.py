# weather_app/views.py
from django.shortcuts import render
from django.http import HttpResponse
import requests
from .models import WeatherData

def get_weather_data(city_name):
    api_key = "3f6a95ab33bce892297dd07ac4b8e10d"
    api_url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}'

    response = requests.get(api_url)
    data = response.json()

    if response.status_code == 200:
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        return temperature, humidity
    else:
        return None, None

def index(request):
    if request.method == 'POST':
        city_name = request.POST['city']
        temperature, humidity = get_weather_data(city_name)
        temperature = round(temperature - 273.15, 2)

        if temperature is not None and humidity is not None:
            weather_data = WeatherData(city=city_name, temperature=temperature, humidity=humidity)
            weather_data.save()

            return render(request, 'base/base.html', {'city': city_name, 'temperature': temperature, 'humidity': humidity})
        else:
            return HttpResponse('Error fetching weather data.')

    return render(request, 'base/index.html')
