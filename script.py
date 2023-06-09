import requests
import matplotlib.pyplot as plt

def fetch_weather_data(api_key, location):
	url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_key}"
	response = requests.get(url)
	data = response.json()
	return data

KEY = "19dc74c37a1a815b3e8e24f9e3706d52"
LOCATION = "27278"

print(fetch_weather_data(KEY, LOCATION))
