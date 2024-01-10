from django.shortcuts import render
import urllib.request
import json


# Create your views here.
def weather(request):
    if request.method == "POST":
        city = request.POST["city"]
        source = urllib.request.urlopen(
            "http://api.openweathermap.org/data/2.5/weather?q=" + city + "&units=metric&appid=20f4f069575188b50abe9a68e39c45f5").read()
        list_of_data = json.loads(source)
        print(list_of_data)
        data = {
            "weather": str(list_of_data["weather"][0]["main"]),
            "icon": str(list_of_data["weather"][0]["icon"]),
            "feels_like": str(list_of_data["main"]["feels_like"]) + "°C",
            "city": str(list_of_data["name"]),
            "country": str(list_of_data["sys"]["country"]),
            "temp": str(list_of_data["main"]["temp"]) + "°C",
            "pressure": str(list_of_data["main"]["pressure"]),
            "humidity": str(list_of_data["main"]["humidity"]),
            "wind": str(list_of_data["wind"]["speed"]) + "m/s",
        }
        # print(data)
    else:
        data = {}
    return render(request, "weather.html", data)
