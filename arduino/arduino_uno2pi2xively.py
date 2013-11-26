#!/usr/bin/python
import xively
import datetime
import serial
import time

ser =serial.Serial('/dev/ttyS1',57600)
ser.readline()

time.sleep(10)

API_KEY ='h0rYyiJftURI3ToAcCziEf4ZGNkk9nrI741NdGzGTnRwQDjx'
FEED_ID = 222032546
api = xively.XivelyAPIClient(API_KEY)
feed = api.feeds.get(FEED_ID)

ser.readline()
ser.readline()
val = ser.readline()
ser.close()
sensorsdata=val.strip("[]\r\n").split(",")
print sensorsdata

Temperature_SHT20 = sensorsdata[0]
RHumidity_SHT20 = sensorsdata[1]
Pressure_BMP180 = sensorsdata[2]
Illuminance_BH1750 = sensorsdata[3]

try:
	datastream = feed.datastreams.get("Temperature_SHT20")
except:
	datastream = feed.datastreams.create("Temperature_SHT20")

datastream.current_value = Temperature_SHT20
datastream.at = datetime.datetime.utcnow()
datastream.update()

try:
	datastream = feed.datastreams.get("Pressure_BMP180")
except:
	datastream = feed.datastreams.create("Pressure_BMP180")

datastream.current_value = Pressure_BMP180
datastream.at = datetime.datetime.utcnow()
datastream.update()

try:
	datastream = feed.datastreams.get("RHumidity_SHT20")
except:
	datstream = feed.datastreams.create("RHumidity_SHT20")

datastream.current_value = RHumidity_SHT20
datastream.at = datetime.datetime.utcnow()
datastream.update()

try:
	datastream = feed.datastreams.get("Illuminance_BH1750")
except:
	datastream =  feed.datastreams.create("Illuminance_BH1750")

datastream.current_value = Illuminance_BH1750
datastream.at = datetime.datetime.utcnow()
datastream.update()
