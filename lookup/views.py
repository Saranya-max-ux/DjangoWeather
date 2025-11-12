from django.shortcuts import render
import json
import requests

def home(request):
    api = None
    api_key = "cfbb60d639dc99f37674bba08891e383"  # put your real API key
    if request.method == 'POST':
        city = request.POST.get('city')
        if city.lower() == "palamaner":
            api_url = f"https://api.openweathermap.org/data/2.5/weather?lat=13.2001&lon=78.7452&appid=cfbb60d639dc99f37674bba08891e383&units=metric"
        else:
            api_url = f"https://api.openweathermap.org/data/2.5/weather?q={city},IN&appid=cfbb60d639dc99f37674bba08891e383&units=metric"
        try:
            api_requests = requests.get(api_url)
            print("API Response:", api_requests.text)
            api = json.loads(api_requests.content)
        except Exception as e:
            print("Error:", e)
            api = "Error......"
    return render(request, 'home.html', {'api': api})

def about(request):
    return render(request, 'about.html')
