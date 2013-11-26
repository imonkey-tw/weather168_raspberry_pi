#!/usr/bin/python
import xively
import datetime
import time
from Adafruit_BMP085 import BMP085

BMP180 = BMP085(0x77)

API_KEY ='TVzWZitAckDLe0iV7gXeyLLR8w6d9gkkzeULjjotb634AjqB'
FEED_ID = 959842380
api = xively.XivelyAPIClient(API_KEY)
feed = api.feeds.get(FEED_ID)


Pressure_BMP180 = round(BMP180.readPressure()/1000.0 , 2)

try:
	datastream = feed.datastreams.get("Pressure_BMP180")
except:
	datastream = feed.datastreams.create("Pressure_BMP180")

datastream.current_value = Pressure_BMP180
datastream.at = datetime.datetime.utcnow()
datastream.update()



