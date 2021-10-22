#inside of email
import urllib.request
import json
from variables import *

city = "Poltava"
temperature = 10
url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={apiKey}"


#Function to take out weather from json file
def readWeather(data):
    JSONdata = json.loads(data)
    tempK = JSONdata["main"]["temp"]
    temp = round(tempK-273.15)
    return(temp)


webUrl = urllib.request.urlopen(url)
#print("Status is:", webUrl.getcode())
if webUrl.getcode() == 200:
    data = webUrl.read()
    readWeather(data)

