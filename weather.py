import requests

API_KEY = "bfbe201d838a3a0822f06fcab9e5e488"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)
    data = response.json()  # Convert response to Python dictionary


    # Check if the API returned a successful response
    if data.get("cod") == 200:
        weather_desc = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]

        return f"The weather in {city} is {weather_desc} with a temperature of {temperature}°C and humidity of {humidity}%."
    
    else:
        return f"Error: {data.get('message', 'Could not fetch data.')}"
