'''Get weather data.'''

import os
import requests
import json

def weather() -> str: 
  """Get the weather from OpenWeather.
  
  Returns:
    Formatted string containing weather stuff
  """
  lat = 43.1566
  lon = 77.6088
  key = os.getenv("OW_TOKEN")
  string = "Weather:\n"

  r = requests.get("https://api.openweathermap.org/data/2.5/weather?lat={" + lat + "&lon="+ lon + "&appid=" + key)
  # process response
  response = json.load(r)
  # https://openweathermap.org/current#one
  # https://openweathermap.org/current#format

  return string