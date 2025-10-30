import requests
import time
import os
from datetime import datetime

def get_weather_data(city, api_key):
    """Fetch weather data from OpenWeatherMap API."""
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:

        response = requests.get(url)
        
        if response.status_code == 200:
            return response.json()
        else:
            print(f"Error: Unable to fetch weather data for {city}. Status code: {response.status_code}")
            return None
        
    except Exception as e:
        print(f"error: {e}")
        return None

def display_weather(data):
    """Display weather information."""
    if not data:
        print("no weather data available ")
        return
    
    print(f"City: {data['name']}")
    print(f"Temperature: {data['main']['temp']}°C")
    print(f"feels like: {data['main']['feels_like']}°C")
    print(f"Weather: {data['weather'][0]['description']}")
    print(f"Humidity: {data['main']['humidity']}%")
    print(f"Wind Speed: {data['wind']['speed']} m/s")

def main():
    """Main function to run the weather monitor."""
    city = input("Enter city name: ")
    api_key = "c99a310e052807bd1589487d266a4365"   

    weather_data = get_weather_data(city, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main() 
