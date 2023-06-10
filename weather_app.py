import requests
import matplotlib.pyplot as plt



def display_weather_data(data):
	# Extract relevant information from the data and display it in a user-friendly format

	forecast = data['list']
	
	print(f"\n{len(forecast)}-Day Forecast:")

	for day in forecast:
		print("\nDate/Time:", day['dt_txt'])
		print("Temperature:", int(day['main']['temp'])-273, "°C")
		print("Humidity:", int(data['list'][0]['main']['humidity']), "%")
		
		print("Min Temperature:", int(day["main"]["temp_min"])-273, "°C")
		print("Max Temperature:", int(day["main"]["temp_max"])-273, "°C")
		print("Pressure:", day["main"]["pressure"])
		print("Weather:", day["weather"][0]["description"])
		print("Wind Speed:", day["wind"]["speed"])
		print("Wind Degree:", day["wind"]["deg"])
		print("Clouds:", day["clouds"]["all"])
		print("---------------")


def visualize_weather_data(data):
	# Extract relevant data for visualization (e.g., temperature, humidity) and plot a graph
	forecast = data['list']
	dates = [day['dt_txt'] for day in forecast]
	temperatures = [int(day['main']['temp'])-273 for day in forecast]
	humidities = [int(data['list'][0]['main']['humidity']) for day in forecast]

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
	api_key = ""
	data = fetch_weather_data(api_key)
	display_weather_data(data)
	visualize_weather_data(data)
    
if __name__ == '__main__':
	main()
