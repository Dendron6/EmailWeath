from apiweather import *
from datetime import datetime

temp = readWeather(data)

def condition():
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S %Y")
    if temp < temperature:
        return(f"\nThis is automated weather report\n\nTemperature in {city} is {temp} degree Celsius\n\nSent with love, sent with care\n{current_time}")

