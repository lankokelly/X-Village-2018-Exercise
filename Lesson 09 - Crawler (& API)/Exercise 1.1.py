import json
import requests

url = 'https://www.metaweather.com/api/location/2306179/'
r = requests.get(url)
#r.encoding = 'utf-8' 
# print(r.text)
data = json.loads(r.text) #data is dict
#print(len(data)) #length=12
#print(data.keys()) 
#print(data.get('consolidated_weather'))
consolidated_list = data.get('consolidated_weather')
consolidated_list = consolidated_list[0]
weather = consolidated_list.get('weather_state_name')
print(weather) #Light Rain