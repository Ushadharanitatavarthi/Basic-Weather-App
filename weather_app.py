
import os
import requests
from dotenv import load_dotenv

# Load API key from the .env file
load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

GEOCODING_URL = "https://api.openweathermap.org/geo/1.0/direct"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """Fetch current weather information for a city."""

    # Find the city's geographical coordinates
    geo_params = {
        "q": city,
        "limit": 1,
        "appid": API_KEY
    }

    geo_response = requests.get(
        GEOCODING_URL,
        params=geo_params,
        timeout=10
    )
    geo_response.raise_for_status()

    locations = geo_response.json()

    if not locations:
        print("\nCity not found. Please enter a valid city name.")
        return

    latitude = locations[0]["lat"]
    longitude = locations[0]["lon"]

    # Request weather information using coordinates
    weather_params = {
        "lat": latitude,
        "lon": longitude,
        "appid": API_KEY,
        "units": "metric"
    }

    weather_response = requests.get(
        WEATHER_URL,
        params=weather_params,
        timeout=10
    )
    weather_response.raise_for_status()

    weather_data = weather_response.json()

    # Extract weather details
    city_name = weather_data["name"]
    temperature = weather_data["main"]["temp"]
    feels_like = weather_data["main"]["feels_like"]
    humidity = weather_data["main"]["humidity"]
    description = weather_data["weather"][0]["description"]
    wind_speed = weather_data["wind"]["speed"]

    # Display weather information
    print("\n" + "=" * 40)
    print("          CURRENT WEATHER")
    print("=" * 40)

    print(f"City          : {city_name}")
    print(f"Temperature   : {temperature} °C")
    print(f"Feels Like    : {feels_like} °C")
    print(f"Weather       : {description.title()}")
    print(f"Humidity      : {humidity}%")
    print(f"Wind Speed    : {wind_speed} m/s")

    print("=" * 40)


def main():
    print("=" * 40)
    print("           BASIC WEATHER APP")
    print("=" * 40)

    if not API_KEY:
        print("API key not found. Please check your .env file.")
        return

    while True:
        city = input("\nEnter city name: ").strip()

        if not city:
            print("City name cannot be empty.")
            continue

        try:
            get_weather(city)

        except requests.exceptions.Timeout:
            print("Request timed out. Please try again.")

        except requests.exceptions.HTTPError as error:
            if error.response.status_code == 401:
                print("Invalid or inactive API key.")
            else:
                print(f"Weather API error: {error}")

        except requests.exceptions.RequestException as error:
            print(f"Connection error: {error}")

        again = input(
            "\nCheck another city? (yes/no): "
        ).strip().lower()

        if again not in ("yes", "y"):
            print("\nThank you for using the Weather App!")
            break


if __name__ == "__main__":
    main()
