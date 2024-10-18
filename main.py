import requests
import time
import schedule
from config import API_KEY, CITIES, ALERT_THRESHOLD_TEMP

def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to retrieve data for {city}")
        return None

def kelvin_to_celsius(temp_k):
    return temp_k - 273.15

def process_weather_data():
    for city in CITIES:
        data = get_weather(city)
        if data:
            temp_c = kelvin_to_celsius(data['main']['temp'])
            feels_like_c = kelvin_to_celsius(data['main']['feels_like'])
            weather_condition = data['weather'][0]['main']
            print(f"{city}: {weather_condition}, Temp: {temp_c:.2f}°C, Feels like: {feels_like_c:.2f}°C")

            # Check if temperature exceeds the threshold and alert
            if temp_c > ALERT_THRESHOLD_TEMP:
                print(f"Alert: {city} has exceeded the temperature threshold of {ALERT_THRESHOLD_TEMP}°C!")

def start_monitoring():
    schedule.every(5).minutes.do(process_weather_data)
    
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    print("Starting Weather Monitoring...")
    start_monitoring()
