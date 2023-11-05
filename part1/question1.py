def get_city_temperature(city):
   if city == "Quito":
      return 22
   elif city == "Sao Paulo":
      return 17
   elif city == "San Francisco":
      return 16
   elif city == "New York":
      return 14

def get_city_weather(city):
  
  sky_condition = None
  if city == "Quito":
     sky_condition = "sunny"
  elif city == "Sao Paulo":
     sky_condition = "cloudy"
  elif city == "New York":
     sky_condition = "rainy"
  temperature = get_city_temperature(city)
  return str(temperature) + " degrees and " + sky_condition