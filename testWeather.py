import requests
from dotenv import load_dotenv
import os

load_dotenv()

def get_weather(city):
    token = os.getenv('API_KEY')
    URL = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}' #change weather to forecast for 5 day forecast
    
    try:
        response = requests.get(URL)
        data = response.json()
        if response.status_code == 200:
            weather_data = {
                'city': data['name'],
                'temperature': data['main']['temp'],
                'humidity': data['main']['humidity'],
                'pressure': data['main']['pressure'],
                'wind_speed': data['wind']['speed']
            }
            return weather_data
        else:
            return None
    except Exception as e:
        print(f'Error: {e}')
        return None