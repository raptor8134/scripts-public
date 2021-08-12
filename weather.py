#!/bin/python3
import time                     # To make suntime work
start_time = time.time()
import json                     # To parse the output from the geoip api
import requests                 # To get all the data we need
from bs4 import BeautifulSoup   # To extract the weather data
from suntime import Sun         # To get sunset and sunrise times
from datetime import datetime   # To make utc2local work
import sys                      # To take command line arguments

# Gets location from geoip database
loc = json.loads(requests.get("http://ip-api.com/json/").text)
lat = round(loc['lat'],2)
lon = round(loc['lon'],2)

try:
    if sys.argv[1] == ("--location" or "-location" or "-l"):
        print(str(lat) + "," + str(lon))

except:
    # Function to convert from UTC to localtime
    def utc2local (utc):
        epoch = time.mktime(utc.timetuple())
        offset = datetime.fromtimestamp (epoch) - datetime.utcfromtimestamp (epoch)
        return utc + offset

    
    # I didn't write this so I don't know what it does
    fart = requests.get('https://weather.com/weather/today/l/'+str(lat)+','+str(lon)+'?par=google&temp=f')
    soup = BeautifulSoup(fart.text, 'html.parser')
    tmp = soup.find("span", class_="CurrentConditions--tempValue--3KcTQ")
    status = soup.find("div", class_="CurrentConditions--phraseValue--2xXSr")

    # Gets sunrise/sunset times and converts them out of UTC to localtime
    sun = Sun(lat, lon)
    sunrise = int(utc2local(sun.get_sunrise_time()).strftime("%H%M"))
    sunset  = int(utc2local(sun.get_sunset_time()).strftime("%H%M"))

    # Gets the correct thingy in the sky 
    if sunrise < int(time.strftime("%H%M")) < sunset:
        sky = "☀"
    else:
        sky = "☽"

    # See if the script is called normally or in location mode, and return accordingly
    print(status.getText() +" "+ tmp.getText() +" "+ sky)
    
    #print("%s seconds" % (time.time() - start_time))
