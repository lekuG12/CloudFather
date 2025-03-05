import requests
from dotenv import load_dotenv
import os
from datetime import datetime, timedelta

load_dotenv()

def get_weather(city):
    token = os.getenv('API_KEY')
    URL = f'https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={token}&units=metric'
    
    try:
        response = requests.get(URL)
        data = response.json()

        if response.status_code == 200:
            # Get tomorrow's date
            tomorrow = (datetime.now() + timedelta(days=1)).strftime('%Y-%m-%d')
            
            # Find the forecast for tomorrow (usually index 8 for next day noon)
            tomorrow_forecast = None
            for forecast in data['list']:
                forecast_date = datetime.fromtimestamp(forecast['dt']).strftime('%Y-%m-%d')
                if forecast_date == tomorrow:
                    tomorrow_forecast = forecast
                    break
            
            if tomorrow_forecast:
                weather_data = {
                    'city': data['city']['name'],
                    'temperature': round(tomorrow_forecast['main']['temp'], 1),
                    'humidity': tomorrow_forecast['main']['humidity'],
                    'pressure': tomorrow_forecast['main']['pressure'],
                    'wind_speed': tomorrow_forecast['wind']['speed'],
                    'description': tomorrow_forecast['weather'][0]['description'],
                    'date': tomorrow
                }
                return weather_data
        return None
    except Exception as e:
        print(f'Error: {e}')
        return None