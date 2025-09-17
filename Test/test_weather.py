import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))  

from weather_app import WeatherApp

def test_class_exists():
    assert WeatherApp is not None

def test_get_weather_emoji():
    # Thunderstorm
    assert WeatherApp.get_weather_emoji(210) == "⛈"
    # Drizzle
    assert WeatherApp.get_weather_emoji(310) == "🌦"
    # Rain
    assert WeatherApp.get_weather_emoji(500) == "🌧"
    # Snow
    assert WeatherApp.get_weather_emoji(600) == "❄"
    # Clear
    assert WeatherApp.get_weather_emoji(800) == "☀"
    # Clouds
    assert WeatherApp.get_weather_emoji(803) == "☁"
    # Unknown
    assert WeatherApp.get_weather_emoji(999) == ""
