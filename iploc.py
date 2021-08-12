#!/bin/python3
from requests import get
import json

ip = get('https://api.ipify.org').text
loc = json.loads(get("http://ip-api.com/json/"+ip).text)
lat = loc['lat']
lon = loc['lon']

print(lat, lon)
