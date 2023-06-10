import requests
import matplotlib.pyplot as plt



def display_weather_data(data):
	# Extract relevant information from the data and display it in a user-friendly format

	forecast = data['list']
	
	print(f"\n{len(forecast)}-Day Forecast:")

	for day in forecast:
		print(f"\nDate/Time: {day['dt_txt']}")
		print(f"Temperature: {int(day['main']['temp'])-273} °C")
		print(f"Humidity: {int(data['list'][0]['main']['humidity'])} %")
		
		print("Min Temperature:", day["main"]["temp_min"])
		print("Max Temperature:", day["main"]["temp_max"])
		print("Pressure:", day["main"]["pressure"])
		print("Weather:", day["weather"][0]["description"])
		print("Wind Speed:", day["wind"]["speed"])
		print("Wind Degree:", day["wind"]["deg"])
		print("Clouds:", day["clouds"]["all"])
		print("---------------")


def visualize_weather_data(data):
	# Extract relevant data for visualization (e.g., temperature, humidity) and plot a graph
	dates = [day['date'] for day in data['forecast']]
	temperatures = [day['temperature'] for day in data['forecast']]
	humidities = [day['humidity'] for day in data['forecast']]

	plt.plot(dates, temperatures, label='Temperature (°C)')
	plt.plot(dates, humidities, label='Humidity (%)')
	plt.xlabel('Date')
	plt.ylabel('Value')
	plt.title('Weather Trends')
	plt.legend()
	plt.xticks(rotation=45)
	plt.show()


def fetch_weather_data(api_key):
	url = f"http://api.openweathermap.org/data/2.5/forecast?id=524901&appid={api_key}"
	response = requests.get(url)
	data = response.json()
	return data

def main():
	api_key = "19dc74c37a1a815b3e8e24f9e3706d52"

	data = fetch_weather_data(api_key)
	display_weather_data(data)
	visualize_weather_data(data)
    
if __name__ == '__main__':
	main()