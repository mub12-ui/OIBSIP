import requests
from config.secrets import WEATHER_API_KEY

BASE_URL = "http://api.weatherapi.com/v1/current.json"


def get_weather(city):
    """
    Get current weather information.
    """

    params = {
        "key": WEATHER_API_KEY,
        "q": city
    }

    try:
        response = requests.get(BASE_URL, params=params)
        data = response.json()

        if "error" in data:
            return "Sorry, I couldn't find that city."

        city_name = data["location"]["name"]
        country = data["location"]["country"]
        temperature = data["current"]["temp_c"]
        condition = data["current"]["condition"]["text"]

        return (
            f"The weather in {city_name}, {country} is "
            f"{condition} with a temperature of {temperature}°C."
        )

    except Exception:
        return "Unable to fetch weather information."