from django.shortcuts import render
import requests
from decouple import config
from pprint import pprint
from .models import City


def home(request):
    cities = City.objects.all()
    url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}"
    # city = "İstanbul"
    # response = requests.get(url.format(city, config("API_KEY"))).json()
    city_data = []
    for city in cities:
        # print(city)
        response = requests.get(url.format(city, config("API_KEY"))).json()
        # pprint(response)

        data = {
            "city": city,
            "temp": response['main']['temp'],
            "desc": response['weather'][0]['description'],
            "icon": response['weather'][0]['icon']
        }
        city_data.append(data)
    print(city_data)
    context = {
        "city_data": city_data
    }
    return render(request, "weather_app/home.html", context)
