import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather(city):
    token = os.getenv('API_KEY')
    city = "Buea"
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}' #change weather to forecast for 5 day forecast

    response = requests.get(URL)
    data = response.json()

    if response.status_code == 200:
        print(f"Temperature: {data['main']['temp']}C")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Pressure: {data['main']['pressure']}hPa")
        print(f"Wind Speed: {data['wind']['speed']}m/s")
    else:
        print("Error in API request")