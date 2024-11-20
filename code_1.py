# weatherpy.py

import requests
import matplotlib.pyplot as plt
import os

class WeatherPy:
    def _init_(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/"

    def fetch_weather(self, location):
        """Fetch current weather for a given location."""
        endpoint = f"{self.base_url}weather"
        params = {"q": location, "appid": self.api_key, "units": "metric"}
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.json()}

    def fetch_forecast(self, location):
        """Fetch 7-day forecast for a location."""
        endpoint = f"{self.base_url}forecast/daily"
        params = {"q": location, "cnt": 7, "appid": self.api_key, "units": "metric"}
        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return {"error": response.json()}

    def plot_temperature_trends(self, forecast_data):
        """Plot temperature trends from forecast data."""
        days = [day['dt'] for day in forecast_data['list']]
        temps = [day['temp']['day'] for day in forecast_data['list']]
        plt.figure(figsize=(10, 5))
        plt.plot(days, temps, marker='o', color='b')
        plt.title('7-Day Temperature Trend')
        plt.xlabel('Days')
        plt.ylabel('Temperature (°C)')
        plt.grid(True)
        plt.show()

# Example Usage
if _name_ == "_main_":
    api_key = "your_openweathermap_api_key"
    weather = WeatherPy(api_key)
    location = "New York"
    
    # Current Weather
    current_weather = weather.fetch_weather(location)
    print("Current Weather:", current_weather)

    # Forecast
    forecast = weather.fetch_forecast(location)
    if "error" not in forecast:
        weather.plot_temperature_trends(forecast)
    else:
        print("Error:", forecast['error'])