'''Get weather data.'''

import os
import requests

def weather() -> str: 
  """Get the weather from OpenWeather.
  
  Returns:
    Formatted string containing weather stuff
  """
  lat
  lon
  #key = os.getenv("OW_TOKEN")
  string = "Weather:\n"
  # 43.1566° N, 77.6088° W
  response = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={" + lat + "&lon="+ lon + "&appid=" + key)

  return string