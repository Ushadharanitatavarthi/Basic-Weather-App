# Basic Weather App

## Project Description
The Basic Weather App is a Python-based application that retrieves and displays current weather information for a city entered by the user. It uses the OpenWeather API to fetch real-time weather data.

## Features
- Search for weather information using a city name.
- Display current temperature in Celsius.
- Display feels-like temperature.
- Show weather conditions.
- Display humidity percentage.
- Display wind speed.
- Handle invalid city names.
- Handle empty input.
- Handle API and connection errors.
- Check weather information for multiple cities.

## Technologies Used
- Python
- OpenWeather API
- Requests
- Python-dotenv

## Project Structure

```text
BasicWeatherApp/
│
├── weather_app.py
├── .env
├── .gitignore
├── README.md
└── screenshots/
```

## Requirements
- Python 3.x
- OpenWeather API key
- Requests library
- Python-dotenv library

## Installation and Setup

**1. Clone the repository**

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
```

**2. Navigate to the project folder**

```bash
cd BasicWeatherApp
```

**3. Install the required packages**

```bash
pip install requests python-dotenv
```

**4. Configure the API key**

Create a `.env` file in the project folder and add:

```text
OPENWEATHER_API_KEY=your_actual_api_key
```

Replace `your_actual_api_key` with your OpenWeather API key.

**5. Run the application**

```bash
python weather_app.py
```

## Sample Output

```text
========================================
           BASIC WEATHER APP
========================================

Enter city name: Hyderabad

========================================
          CURRENT WEATHER
========================================
City          : Hyderabad
Temperature   : [Temperature] °C
Feels Like    : [Feels Like] °C
Weather       : [Weather Description]
Humidity      : [Humidity]%
Wind Speed    : [Wind Speed] m/s
========================================

Check another city? (yes/no):
```

*Note: Weather values change depending on the current weather conditions.*

## Error Handling
- Displays a message when the city name is invalid.
- Handles empty city input.
- Handles invalid or inactive API keys.
- Handles connection errors and request timeouts.

## Security
The API key is stored in the `.env` file and should not be uploaded to GitHub. The `.gitignore` file excludes sensitive configuration files.

## Conclusion
The Basic Weather App demonstrates the use of Python, API integration, and error handling to retrieve and display current weather information for different cities.
